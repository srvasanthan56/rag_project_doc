# CENDICT Part 1 ETL — RAG Knowledge Document

## Purpose

This document explains, step by step, what happens in the
`Flows/generalFlow/cendict_part1_etl` application. It combines the notebooks,
Informatica-style specifications, store and dictionary SQL, and the
`DICTWK2_COPY.pli` comparison notes.

The ETL replaces a monolithic mainframe `DICTWK2` process with Spark
DataFrame components and PostgreSQL dictionary access.

## Complete flow

```text
1_Linker
  ├─ 2.1 MOVEIN → 3_A → 3_IS_1 → 3_IS_2 → 3_IS_3 → 3_IS_4 → 3_IS_5 → 3_IS_6
  │                                                    │
  └─ 2.3 STORMKT ─────────────────────────────────────┘
                                                       ↓
                                      4_ MOVEIN × STORMKT
                                                       ↓
                           4_A → 4_IS_1 → 4_IS_2 → 4_IS_3
                                                       ↓
                                 5_validate → 6_Fixer1
                                                       ↓
                                          7_validatePreDict
                                      ┌────────┴────────┐
                                  regular        skip_dictionary
                                      │                  │
                         2.2 KEYCAT ─┴─ 8_linker       │
                                      ↓                  │
                              9_Main_Dict_Read           │
                                      ↓                  │
                              result branch ─────────────┘
                               ┌──────────────┐
                         10.1 NEWITEM   10.2 consolidate
                               └──────┬───────┘
                                11_Junction → 12_Output
                                  ├─ 13.1 → 13.1.1 NewItemFile
                                  ├─ 13.2 → 13.2.1 causal trigger
                                  └─ 13.3 Logger
```

`2.2_KEYCAT` and `2.3_STORMKT_DB` are parallel components. They are not a
mandatory `2.1 → 2.2 → 2.3` chain.

## Runtime and DataFrame conventions

- `context.getDataFrames()` reads DataFrames published by upstream components.
- `context.saveDataFrames({...})` publishes named DataFrames.
- `context.setInputs({...})` publishes runtime flags and counters.
- Important parameters include `COUNTRY`, `WEEK`, `UPDATE`, `STORE_TABLE`,
  `MF_*`, `PATH_PREFIX`, `env`, `COUNTRY_CC`, and `JOB_LOG_PREFIX`.
- Some notebooks read `list(dfs.keys())[0]`. This is an orchestration
  contract: the expected primary frame must be first in the context.
- `SYSPRINT` and `LETTPC` are operational logs. Current Spark behavior logs
  these events; it does not reproduce live mainframe mail.

---

## Component 1 — `1_Linker.ipynb`

**Path:** `Flows/generalFlow/cendict_w_snippet/flow/1_Linker.ipynb`

**Purpose:** Initialize and validate the run before Part 1 starts.

**What happens:**

1. Read and flatten `ISContent` and flow parameters.
2. Build dictionary and store database configuration.
3. Read dictionary row count and `country_id`.
4. Validate the dictionary database against `COUNTRY`.
5. Read country/cluster `cenparm` values from the store database.
6. Derive `comb` and `isCausalProcess`.
7. Publish `oldDictCount`, `isValidDictDatabase`, `comb`, and
   `isCausalProcess`.
8. Save a one-row `inputs` DataFrame.

**Outputs:** runtime flags plus `inputs`.

**Parity note:** the saved `inputs` row can be stale if the parameter
dictionary is created before `setInputs` and not rebuilt afterward.

---

## Component 2.1 — `2.1_valid_MOVEIN.ipynb.ipynb`

**Input:** `TRUE`  
**Output:** `movein_raw_parsed`  
**Runtime output:** `movein_count`

This component establishes the raw MOVEIN contract.

1. Read the DataFrame named `TRUE`.
2. Save it unchanged as `movein_raw_parsed`.
3. Count rows and publish `movein_count`.
4. Optionally inspect rows whose movement values are all zero.

Only the MOVEIN line starts here. The output feeds `3_A_SORTUPC`.

---

## Component 2.2 — `2.2_KEYCAT.ipynb.ipynb`

**Output:** `KEYCAT_TABLE`

This component builds the country-specific key-category allow-list.

1. Build the common input path from country and environment parameters.
2. Read the BPPR/key-category file using FTP or local storage.
3. If the external file is unavailable, use the country master list embedded
   in the notebook.
4. Create `PIC_KEYCAT` and `KEYCAT_FLAG`.
5. Save the result as `KEYCAT_TABLE`.

`KEYCAT_TABLE` is a parallel branch. It rejoins `regular` before
`8_linker`; it is not part of the `4_` store join.

---

## Component 2.3 — `2.3_STORMKT_DB.ipynb.ipynb`

**Input:** country/environment `STORE_TABLE` through JDBC  
**Output:** `stormkt`

This component creates the store-master lookup used to enrich MOVEIN rows.

1. Read the configured store view/table through Spark JDBC.
2. Project the source into the expected STORMKT layout.
3. Alias `iri_store_num` as `STRNUM`.
4. Coalesce nullable `FACTOR` and `AUDIT_FLAG` values.
5. Cast selected columns to integer types.
6. Validate the country.
7. For Germany, apply week-open/week-closed filtering.
8. Deduplicate by `STRNUM`.
9. Save as `stormkt`.

The Spain example view is `es_store_master_view.sql`. The notebook stays
generic because the actual source is supplied by `STORE_TABLE`.

---

## Component 3.A — `3_A_SORTUPC.ipynb.ipynb`

**Input:** `movein_raw_parsed`  
**Output:** `TEMP`  
**Runtime output:** `ZEROSTR`

This is the Spark equivalent of the early `SORTUPC` preparation stage.

1. Read MOVEIN rows.
2. Sort ascending by `T_SYSTEM`, `T_VENDOR`, `T_ITEM`, and `NEW_STORE#`.
3. Save ordered rows as `TEMP`.
4. Detect invalid UPC ranges.
5. Check row `WEEK` against runtime `WEEK`; the current code treats a
   mismatch as an error.
6. Detect rows where both `NEW_STORE#` and `IRI_STORE#` are zero.
7. Publish `ZEROSTR`.
8. Write `SYSPRINT` and `LETTPC` logs and optionally upload them.

---

## Component 3.IS.1 — `3_IS_1_BAD_STORENUMBER_CHECK.md`

**Input:** `TEMP`  
**Purpose:** Remove rows with unusable movement store identifiers.

Keep rows where at least one of `NEW_STORE#` or `IRI_STORE#` is non-null and
non-zero. Invalid rows cannot be reliably resolved in STORMKT.

---

## Component 3.IS.2 — `3_IS_2_checkUPC_STORENUM.md`

**Input:** output of `3_IS_1`  
**Purpose:** Calculate UPC and store validation fields.

This stage derives `StoreNumber`, translated UPC values, `isTotalUpc`,
`isValidUpc`, and `isSkipRecord`. It also preserves owner UPC values for rows
whose translated UPC is zero.

---

## Component 3.IS.3 — `3_IS_3_Assigning_T_UPC.md`

**Input:** output of `3_IS_2`  
**Purpose:** Move temporary UPC calculations into canonical fields.

Temporary values are assigned to `T_SYSTEM`, `T_VENDOR`, `T_ITEM`,
`NEW_STORE#`, and `ALPHA_DESCR`. The resulting names match the downstream
dictionary row contract.

---

## Component 3.IS.4 — `3_IS_4_valid_UPC_Records.md`

**Input:** output of `3_IS_3`  
**Purpose:** Keep only processable UPC rows.

Keep rows where `isSkipRecord` is false. Rows marked for skipping leave the
normal MOVEIN refinement line.

---

## Component 3.IS.5 — `3_IS_5_UNSCALE_DOLLARS.md`

**Input:** valid UPC rows  
**Purpose:** Convert scaled measures into dictionary-ready values.

Apply the `MULT`/unscale rules to temporary unit and dollar fields, including
`MOVE_UNITS_Temp` and `MOVE_DOLLARS_Temp`.

---

## Component 3.IS.6 — `3_IS_6_drop_udf_UpcFlags_Sc.md`

**Input:** output of `3_IS_5`  
**Purpose:** Finalize the MOVEIN schema before the store join.

Promote temporary measures to `MOVE_UNITS`, `MOVE_DOLLARS`, and related
canonical fields. Drop temporary, UDF, UPC-flag, and scaling helper columns.
The result becomes the left input of the `4_` join.

---

## Component 4 — `4_2.3-3_IS_movein_w_stormkt.md`

**Left input:** output of `3_IS_6`  
**Right input:** `stormkt`  
**Join key:** `StoreNumber = STRNUM`

This component attaches store-master information to each refined movement
row. It adds market, store type, service, chain, audit, factor, footprint,
and week fields. It is a join specification, not a separately named
`junction` notebook.

`KEYCAT_TABLE` is not used in this join. It rejoins later before `8_linker`.

---

## Component 4.A — `4_A_Fixer.ipynb`

**Input:** joined MOVEIN × STORMKT  
**Outputs:** `movein_w_stormkt`, `dict_log`  
**Runtime output:** `uniqueStoreCount`

This component performs store hygiene and store-level diagnostics.

1. Count distinct non-null `StoreNumber` as `uniqueStoreCount`.
2. Count inbound rows by `STRNUM`.
3. Drop rows where both movement store numbers are zero.
4. Derive an effective store identifier.
5. Drop blank effective stores and non-zero stores with no `STRNUM` join.
6. Trim `STRTYP`.
7. Convert `I`, `E`, `H`, and `F` store types to `D`.
8. Drop rows whose normalized `STRTYP` is blank.
9. Count invalid `RECORD_TYPE` rows per `STRNUM` as `BAD_COUNT`.
10. Count zero movement rows per `STRNUM` as `ZER_COUNT`.
11. Create `dict_log` from the inbound and quality counts.
12. Save valid enriched rows as `movein_w_stormkt`.

---

## Component 4.IS.1 — `4_IS_1_movein_w_storinfo_has.md`

**Input:** `movein_w_stormkt`

Derive STORINFO fields from the store-master columns:

- `STORINFO_MARKET`
- `STORINFO_TYPE`
- `STORINFO_SERV_TYPE`
- `STORINFO_CHAIN_ID`
- `STORINFO_SEND`
- `STORINFO_AUDIT`
- `STORINFO_FACTOR`
- `STORINFO_SUBTRACT`
- `STORINFO_STORE_Tmp`
- `isStorInfoTypeValid`

`STORINFO_SEND` is `Y` when the store send indicator is `1`, otherwise `N`.
Audit and factor values depend on `AUDIT_FLAG` and related audit fields.
Blank store types are marked invalid.

---

## Component 4.IS.2 — `4_IS_2_validateStorinfo.md`

**Input:** output of `4_IS_1`

Keep rows where the STORINFO validation flag is true. The specifications
refer to both `isStorinfo` and `isStorInfoTypeValid`; implementation must
map these names consistently.

---

## Component 4.IS.3 — `4_IS_3_drop_storinfo_flags.md`

**Input:** output of `4_IS_2`  
**Output:** `drop_storinfo_flags`

Finalize the pre-validation schema:

1. Drop `StoreNumber` where required by the final layout.
2. Rename `STORINFO_STORE_Tmp` to `STORINFO_STORE`.
3. Normalize `Week_opened` to `week_opened`.
4. Normalize `Week_closed` to `week_closed`.
5. Remove helper and non-final columns.
6. Save using the component contract `drop_storinfo_flags`.

This is the explicit input to `5_validate`.

---

## Component 5 — `5_validate.ipynb`

**Input:** `drop_storinfo_flags`  
**Output:** `validated_movein`

This component performs country rules, hard movement validation, price
preparation, and description cleanup.

1. Create optional input counts grouped by `NEW_STORE#`.
2. Detect null or zero `MKTNUM` and log affected stores.
3. Normalize `STORINFO_MARKET`: UK `E→1`, Germany `G→3`, France `H→4`,
   Italy/Spain use the country-specific digit from `MKTNUM`.
4. Warn about markets outside `1..192`; invalid market rows are not deleted
   by this warning.
5. Derive `HOL_RAND`, `GER_SYVD`, `UK_PLU`, and `SPA_6PLU`.
6. Cast `MOVE_DOLLARS` to integer.
7. Reject invalid record types: values greater than `4`, or negative values
   other than `9`.
8. Reject rows where `MOVE_DOLLARS`, `MOVE_LBS`, and `MOVE_UNITS` are all zero.
9. Derive `UNIT_PRICE_EXP_Temp`, `FLAGS_EXP_PRICE_Temp`,
   `PRICING_QTY_Temp`, and `IDEAL_UNIT_PRICE_Temp`.
10. Uppercase and normalize `ALPHA_DESCR`.
11. Replace known unknown descriptions with `.`, remove leading `+`/`-`
    markers where required, and replace null descriptions with a blank.
12. Save valid rows as `validated_movein`.

---

## Component 6 — `6_Fixer1.ipynb`

**Input:** first/primary DataFrame, normally `validated_movein`  
**Output:** `valid_movement`

This is a naming/pass-through component. It reads the primary frame placed
first by orchestration and saves it unchanged as `valid_movement`.

---

## Component 6.IS.1 — `6_IS_1_drop_stormktFields.md`

This specification defines the store-master columns dropped or renamed
before the pre-dictionary split. The implementation boundary is the stage
that produces `drop_storinfo_flags`.

---

## Component 7 — `7_validatePreDict.ipynb`

**Input:** primary frame, normally `valid_movement`  
**Outputs:** `regular`, `skip_dictionary`

This component decides whether each row requires dictionary processing.

1. Build `isNotReadDictionary` from record type, UPC systems/vendors, country
   flags, and special PLU conditions.
2. Identify rows that would normally bypass dictionary access.
3. Split those rows using `FOOTPRINT_PLU_XLATED`.
4. `FOOTPRINT_PLU_XLATED = 1` creates `df_leave`; these rows must continue
   through dictionary logic.
5. Other bypass rows create `df_write_move`, which becomes
   `skip_dictionary`.
6. Union normal dictionary rows with `df_leave`.
7. Save that union as `regular`.

**Critical parity rule:** `PLU_XLATED` is an exception to the skip branch,
not a reason to skip the dictionary.

---

## Junction before Component 8

**Inputs:** `regular` and `KEYCAT_TABLE`

The orchestration layer combines the validated regular movement stream with
the parallel key-category table. This is different from the earlier
MOVEIN × STORMKT join.

---

## Component 8 — `8_linker.ipynb`

**Inputs:** `regular`, `KEYCAT_TABLE`  
**Outputs:** `movein_w_stormkt_regular`, `movein_w_stormkt_keycat`

This component prepares stable inputs for the dictionary-read stage. It
publishes the regular movement data and the key-category companion data.
It is a hand-off/naming component; the main dictionary business logic is in
component 9.

---

## Component 9 — `9_Main_Dict_Read.ipynb.ipynb`

**Inputs:** `movein_w_stormkt_regular`, `movein_w_stormkt_keycat`, STORINFO  
**Database inputs:** country-specific `MF_*` tables  
**Output:** `result`

This is the main dictionary processing component and the PostgreSQL
replacement for mainframe dictionary calls.

1. Read regular and key-category movement inputs.
2. Attach STORINFO required for dictionary processing.
3. Open database connections/transactions.
4. Build the composite UPC key from `T_SYSTEM`, `T_VENDOR`, and `T_ITEM`.
5. Read dictionary, market, WAD, WLM, and attribute records.
6. Decide found, not-found, add, rewrite, update, or movement-only behavior.
7. Apply `UPDATE` gating to dictionary writes.
8. Apply dynamic-price and `ignore_record` behavior.
9. Apply HICONE/price-limit logic where enabled.
10. Derive `isNewItem` using description, key-category, week/WLM,
    dictionary-update, and ignore-record conditions.
11. Build the result movement/dictionary row.
12. Commit/close transactions.
13. Save one DataFrame as `result`.

The Spain dictionary DDL example is `es_dictionary.sql`, which describes
core dictionary, market, WAD, and WLM tables. The deployed country uses
runtime `MF_*` names.

Component 9 saves only `result`. The NEWITEM and consolidate copies are
created by orchestration after this component.

---

## Branch after Component 9

The orchestration layer creates two logical copies of `result`:

- NEWITEM branch → component `10.1`
- Consolidate branch → component `10.2`

---

## Component 10.1 — `10.1_NEWITEM.md`

**Input:** NEWITEM copy of `result`  
**Output:** `NEWITEM`

Filter the dictionary result where `isNewItem` is true and publish those
records as `NEWITEM`.

---

## Component 10.2 — `10.2_consolidate.ipynb`

**Inputs:** consolidate copy of `result`, `skip_dictionary`  
**Outputs:** `consolidated`, `storinfo`

1. Read dictionary-processed result rows.
2. Read rows that bypassed dictionary processing.
3. Union compatible rows according to the consolidate rules.
4. Save movement rows as `consolidated`.
5. Save store-information rows as `storinfo`.

---

## Component 11 — `11_Junction.md`

**Inputs:** `NEWITEM`, `consolidated`, `storinfo`

This is currently a specification-level black box. Its documented role is
to combine the three logical outputs before component 12. Detailed internal
join/union behavior remains to be confirmed.

---

## Component 12 — `12_Output.ipynb`

**Outputs:** `NEWITEM`, `consolidated`, `storinfo`

Materialize the three stable outputs needed by the 13.x branches:

1. Save new-item rows as `NEWITEM`.
2. Save consolidated movement rows as `consolidated`.
3. Save store-information rows as `storinfo`.

---

## Component 13.1 — `13.1_ZERO_KEY.md`

**Input:** `NEWITEM`

Filter new-item rows where `KEYCAT = 0`. These records are sent to
`13.1.1_NewItemFile`.

The historical analogue is the `SORTNW1` zero-key selection. The mapping
between historical byte offset `159,2` and Spark `KEYCAT` must be verified.

---

## Component 13.1.1 — `13.1.1_NewItemFile.ipynb.ipynb`

**Input:** zero-key NEWITEM rows

Order and shape the selected new-item rows, then save the terminal new-item
file/data using the notebook's dynamic output key.

---

## Component 13.2 — `13.2_WKBPCM2.ipynb`

**Input:** `consolidated`  
**Output:** `consolidated`

Apply WKBPCM2 combination logic to collapse/merge duplicate movement rows.
The historical analogue is the `COMBINE WKBPCM2` stage. Compare ordering
with the historical `SORTDATA` rules when exact parity is required.

---

## Component 13.2.1 — `13.2.1_triggerCausalDict.ipynb`

**Input:** output of `13.2_WKBPCM2`  
**Runtime output:** `runnow`

Determine whether the next causal-dictionary/Part 2 flow should run, publish
`runnow`, and trigger the downstream `EURO_CENDICT_PART2`-type process when
required. This is the center branch and the last component ending the main
Part 1 job thread.

---

## Component 13.3 — `13.3_Logger.ipynb`

**Input:** `storinfo`

Log or persist the store-information output for operational and audit use.
This branch is parallel to the NEWITEM and consolidated branches.

---

## Mainframe responsibility mapping

| Mainframe responsibility | ETL component |
|---|---|
| Parameter validation | `1_Linker` and runtime configuration |
| Read KEYCAT input | `2.2_KEYCAT`, `8_linker` |
| Sort MOVEIN | `3_A_SORTUPC` |
| UPC/store preparation | `3_IS_1` through `3_IS_6` |
| Store master lookup | `2.3`, `4_`, `4_A` |
| STORINFO derivation | `4_IS_1` through `4_IS_3` |
| Country flags and movement validation | `5_validate` |
| Dictionary bypass decision | `7_validatePreDict` |
| Dictionary read/update | `9_Main_Dict_Read` |
| New-item processing | `9`, `10.1`, `13.1`, `13.1.1` |
| Movement consolidation | `10.2`, `13.2_WKBPCM2` |
| Causal trigger | `13.2.1_triggerCausalDict` |
| Store-information logging | `13.3_Logger` |

---

## Important parity and implementation gaps

1. Verify every database write in component 9 obeys `UPDATE=0` read-only mode.
2. Compare dictionary generation/add/rewrite behavior with `DCTRDX`,
   `DCTWRTX`, and `DCTUPDX`.
3. Verify that historical `SORTNW1` offset `159,2` means the same thing as
   Spark `KEYCAT = 0`.
4. Compare WKBPCM2 sorting and deduplication with historical `SORTDATA`.
5. Confirm full HICONE behavior for each country.
6. Decide whether `TRAK`, `SMF`, and DICTWK2 counters need Spark equivalents.
7. Ensure wider DAG coverage for `PREPCAUS`, `CAUSAL`, `COPYMOVE`, and
   `SUBMOVE` when comparing the complete legacy job.
8. Resolve `isStorinfo` versus `isStorInfoTypeValid` naming.
9. Redact database and FTP credentials from logs and notebook outputs.
10. Replace positional `list(keys())[0]` reads with explicit DataFrame names
    when stable orchestration contracts are available.

## Source location

Implementation artifacts:

`Flows/generalFlow/cendict_part1_etl/`

Supporting analysis:

`analysis/etl_flow/`
