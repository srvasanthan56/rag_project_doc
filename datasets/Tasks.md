## To DO

Aug 17, 2026

- [ ] be the best   
  - [ ] and take any two upc , go through it all process   
    - [x] ~~Explain how dictionary gets read , show what keys are necessary among all keys~~   
    - [x] ~~TGENERATION , KEYCAT, MFBCAT~~  
      - [x] ~~Explain UPC, how it changes ,~~  
      - [x] ~~KEYCAT, MFBCAT  how keycat is important ,~~   
    - [x] ~~Explain DPO , what is dpo , how it affects price ,~~  
      - [x] ~~go through cursor, get a neat explanation~~  
      - [x] ~~and create or mimic a item which will go through the dpo logic with one example from dictionary~~   
      - [x] ~~Explain how this keycat~~   
    - [x] ~~Explain Hicone , what is hiconing , what it affects~~  
      - [x] ~~again go through cursor , get a neat explanation for each cases~~   
      - [x] ~~create two items that go through~~   
- [ ] rush  
  - [ ] AUDIT FACTOR  1 checks  
  - [ ] Bypass DPO Checks  
- [ ] **PROJECT**  
  - [ ] Based on week and store it should provide all details , like whether census store or sample store, which cluster, what status it belong to once done you can run the phase 2 where we can provide ean and it shows whether dpo taken place, hicone done,   
    - [ ] add   
    - [ ] vvv , verbose, how this works , how help works in subsequent   
    - [ ] learn fuzzy search , markdown finder   
    - [ ] 
      ```
      phase 3 run it can do data comparison, and provide insights  
      ```
  - [ ] [Ultimatum Tasks](https://docs.google.com/document/u/0/d/1w0mAz_8BmWoNEvxalBa6kkwI7z-q50yiZbIFSkysWj4/edit)  
- [ ] **What fields get dictionary update**   
  - [ ] **Write new test cases for Hicone , moveunits, dpo , dynamic price , how it affect dictionary price and etc  Phase 1 test ready**   
  - [ ] **TGeneration Changes,   Phase 2 test ready**   
- [ ] Systementals  
  - [ ] **Learn Git problems and simulate it**   
  - [ ] fluent python fobject and datamodels  generators, listcomp  
  - [ ] Jump Game  
  - [ ] Next Permutation  
  - [ ] **Complete data models ch 2** 

Aug 6, 2026

- [ ] be the best   
  - [x] ~~refine the document , go though it~~   
  - [x] ~~Find the iritem values that gets used use , .show to denote it~~   
  - [ ] and take any two upc , go through it all process   
    - [ ] Explain how dictionary gets read , show what keys are necessary among all keys   
    - [ ] TGENERATION , KEYCAT, MFBCAT  
      - [ ] Explain UPC, how it changes ,  
      - [ ] KEYCAT, MFBCAT  how keycat is important ,   
    - [ ] Explain DPO , what is dpo , how it affects price ,  
      - [ ] go through cursor, get a neat explanation  
      - [ ] and create or mimic a item which will go through the dpo logic with one example from dictionary   
      - [ ] Explain how this keycat   
    - [ ] Explain Hicone , what is hiconing , what it affects  
      - [ ] again go through cursor , get a neat explanation for each cases   
      - [ ] create two items that go through   
    - [x] ~~How new items gets produced~~   
    - [ ] and what are the   
  - [ ] least  
    - [x] ~~Storinfo  how these is maintained, which have zero count, important statistics , how logs is written~~   
- [ ] rush  
  - [x] ~~Check ZEROCOUNT~~   
    - [x] ~~Change 2 upc record, and set it to MU as zero and 2 upc with normie~~  
    - [ ] ![][image1]  
  - [ ] Doc  KT  
    - [x] ~~Create new doc ( add it in the DICTWK2), which explains the overview of the process with Screenshots updated~~   
    - [x] ~~Capture what are the outputs schema~~  
    - [x] ~~Payload being used~~  
  - [ ] Bypass DPO Checks  
  - [x] ~~whether updated EUROSCAN.BPPR file is being read~~   
    - [x] ~~check bypass inside main dict read~~   
  - [ ] 
  - [ ] AUDIT FACTOR  1 checks  
  - [x] ~~EUROSCAN.BPPRS file  delete the keycat cache values , test it~~ 



```
from pyspark.sql.functions import col
fil_df = df.filter(col("T_SYSTEM").isin(50,69) & col("T_VENDOR").isin(55028, 76105) & col("T_ITEM").isin(38920,80269))

```

```
from pyspark.sql.functions import col, lit, when

fil_df = (
    fil_df
    .withColumn(
        "MOVE_DOLLARS",
        when(
            (col("T_SYSTEM") == 69) &
            (col("T_VENDOR") == 76105) &
            (col("T_ITEM") == 80269),
            lit(0)
        ).otherwise(col("MOVE_DOLLARS"))
    )
    .withColumn(
        "MOVE_UNITS",
        when(
            (col("T_SYSTEM") == 69) &
            (col("T_VENDOR") == 76105) &
            (col("T_ITEM") == 80269),
            lit(0)
        ).otherwise(col("MOVE_UNITS"))
    )
)

```

Jul 27, 2026

- [ ] watch oddity  
  - [x] ~~Do libin changes~~   
    - [x] ~~add cluster pool in payload for each job~~  
    - [x] ~~Modify request url to include cluster pool~~

```
96    78626    28013700011117
4E    15261    28013700062904
4E    33511    59010123412345 (DPO not applied on IS)
4E    33511    84011047417711
2F    14975    28013700011117
2F    14975    28013700005340
2F    15793    28013700005340
2F    15793    28013700011117 
```

- [ ] **What fields get dictionary update**   
  - [ ] **Write new test cases for Hicone , moveunits, dpo , dynamic price , how it affect dictionary price and etc  Phase 1 test ready**   
  - [ ] **TGeneration Changes,   Phase 2 test ready**   
  - [ ] **EUROSCAN.BPPR files bypass dpo checks**   
  - [ ] **AUDIT FACTOR  1 checks**   
- [ ] **Dictionary ReVamp **   
  - [x] ~~**Dusting off docs**~~  
  - [x] ~~**Understand jcl and flows and segregation**~~  
  - [x] ~~**Check ZERCOUNT**~~  
  - [ ] **Code checking**   
- [ ] Test Audit Jobs  
  - [ ] Germany  77 generate files from Tran , Nagprakash   
  - [ ] Check  audit 42   
- [ ] Systementals  
  - [ ] **Learn Git problems and simulate it**   
  - [ ] fluent python fobject and datamodels  generators, listcomp  
  - [ ] Jump Game  
  - [ ] Next Permutation  
  - [ ] **Complete data models ch 2**   
- [ ] **Run for the audit  for the 2442  42 , 77 and 75 –  Compare**   
  - [x] ~~Add gr country tag for clstdicav2~~  
- [ ] Create a flow which will convert binary file to publish content, csv file to publish content   
  - [ ] automatic  file parsing ability based on ascii or binary   
  - [ ] conv to spark df and save it as publish content and trigger dictionary job   
- [ ] Test trigger utility  using cursor explain how it is working , extract frn files,  
- [x] ~~Test Census Dev for 5 different countries~~   
- [ ] **Remove  validate , codes**   
- [ ] **PROJECT**  
  - [ ] Based on week and store it should provide all details , like whether census store or sample store, which cluster, what status it belong to once done you can run the phase 2 where we can provide ean and it shows whether dpo taken place, hicone done,   
    - [ ] add   
    - [ ] vvv , verbose, how this works , how help works in subsequent   
    - [ ] learn fuzzy search , markdown finder   
    - [ ] 
      ```
      phase 3 run it can do data comparison, and provide insights  
      ```
  - [ ] [Ultimatum Tasks](https://docs.google.com/document/u/0/d/1w0mAz_8BmWoNEvxalBa6kkwI7z-q50yiZbIFSkysWj4/edit)  
- [ ] **Add logs whenever dictionary price gets changed**

Jul 20, 2026

- [x] ~~validation~~  
  - [x] ~~Follow-up Analysis (Country: UK | Week: 2445  801654050280 (82093)  *Price replace didn’t happen , b-14,~~*   
  - [x] ~~Sankar’s task II SP~~  
  - [ ] watch oddity

```
96    78626    28013700011117
4E    15261    28013700062904
4E    33511    59010123412345 (DPO not applied on IS)
4E    33511    84011047417711
2F    14975    28013700011117
2F    14975    28013700005340
2F    15793    28013700005340
2F    15793    28013700011117 
```

- [ ] **What fields get dictionary update**   
  - [ ] **Write new test cases for Hicone , moveunits, dpo , dynamic price , how it affect dictionary price and etc**  
  - [ ] **TGeneration Changes,**   
- [ ] Test Audit Jobs  
  - [ ] Germany  77 generate files from Tran , Nagprakash   
- [ ] Systementals  
  - [ ] **Learn Git problems and simulate it**   
  - [ ] fluent python fobject and datamodels  generators, listcomp  
  - [ ] Jump Game  
  - [ ] Next Permutation  
  - [ ] **Complete data models ch 2**   
- [ ] **Run for the audit  for the 2442  42 , 77 and 75 –  Compare**   
  - [ ] Add gr country tag for clstdicav2  
- [ ] Create a flow which will convert binary file to publish content, csv file to publish content   
  - [ ] automatic  file parsing ability based on ascii or binary   
  - [ ] conv to spark df and save it as publish content and trigger dictionary job   
- [ ] Test trigger utility  using cursor explain how it is working , extract frn files,  
- [ ] Test Census Dev for 5 different countries   
- [ ] **PROJECT**  
  - [ ] Based on week and store it should provide all details , like whether census store or sample store, which cluster, what status it belong to once done you can run the phase 2 where we can provide ean and it shows whether dpo taken place, hicone done,   
    ```
    phase 3 run it can do data comparison, and provide insights  
    ```
  - [ ] [Ultimatum Tasks](https://docs.google.com/document/u/0/d/1w0mAz_8BmWoNEvxalBa6kkwI7z-q50yiZbIFSkysWj4/edit)  
- [ ] **Add logs whenever dictionary price gets changed**



Jul 6, 2026

- [x] ~~**Change SYSRPT  add chain and census name**~~    
- [x] ~~**Comment BYPASS DPO  FOR Holland**~~  
- [x] ~~In manual procs , see FRNBATCH whether chain name is given correctly~~   
- [ ] **What fields get dictionary update**   
  - [x] ~~Create dictionary field test cases~~   
  - [x] ~~Create a simulation run and see what fields gets updated and whether test cases are passing (Everything passed successfully except description due to new changes)~~  
  - [ ] **Write new test cases for Hicone , moveunits, dpo , dynamic price , how it affect dictionary price and etc**  
  - [ ] **TGeneration Changes,**   
- [ ] Test Audit Jobs  
  - [ ] Germany  77 generate files from Tran , Nagprakash   
- [ ] Systementals  
  - [ ] **Learn Git problems and simulate it**   
  - [ ] fluent python fobject and datamodels  generators, listcomp  
  - [ ] Jump Game  
  - [ ] Next Permutation  
  - [ ] **Complete data models ch 2**   
- [ ] **Run for the audit  for the 2442  42 , 77 and 75 –  Compare**   
  - [ ] Add gr country tag for clstdicav2  
- [ ] Create a flow which will convert binary file to publish content, csv file to publish content   
  - [ ] automatic  file parsing ability based on ascii or binary   
  - [ ] conv to spark df and save it as publish content and trigger dictionary job   
- [x] ~~Non DCS  sample UK~~  
- [ ] Test trigger utility  using cursor explain how it is working , extract frn files,  
- [ ] Test Census Dev for 5 different countries   
- [ ] ~~Infoscan prop file change from auxiliary to census/raw~~ [Janaranjan E](mailto:janaranjan.e@blackstraw.ai)  
- [x] ~~CENMERGE  add tag 1 and tag 2 ,~~   
- [ ] **PROJECT**  
  - [ ] Based on week and store it should provide all details , like whether census store or sample store, which cluster, what status it belong to once done you can run the phase 2 where we can provide ean and it shows whether dpo taken place, hicone done,   
    ```
    phase 3 run it can do data comparison, and provide insights  
    ```
  - [ ] [Ultimatum Tasks](https://docs.google.com/document/u/0/d/1w0mAz_8BmWoNEvxalBa6kkwI7z-q50yiZbIFSkysWj4/edit)  
- [ ] **Add logs whenever dictionary price gets changed**

Jun 29, 2026

- [x] ~~UPCSelect  96 Cluster~~  
- [ ] Change SYSRPT  add chain adn census name   
- [ ] fluent python fobject and datamodels   
  - [ ] Jump Game  
  - [ ] Next Permutation  
  - [ ] **Complete data models ch 2**   
- [x] ~~**Teach SQL to vasanthan [Deepti Shankar**](mailto:deepti.shankar@blackstraw.ai)~~  
- [ ] Hicone explanation   
- [ ] **What fields get dictionary update**   
  - [ ] Create dictionary field test cases   
  - [ ] Create a simulation run and see what fields gets updated and whether test cases are passing  
- [ ] Learn about cluster, node, spark   
- [ ] wal, context switch  
- [x] ~~Create automation~~  
- [x] ~~**Check upcmove files**~~   
- [ ] Test Audit Jobs  
  - [ ] Germany  77 generate files from Tran , Nagprakash   
    - [x] ~~week run is 2442, 42, 77, 75 requested files from Nagprakash  Nag ditched , requested files from Tran instead~~  
    - [ ] **Run for the audit  for the 2442  42 , 77 and 75 –  Compare**   
      - [ ] Add gr country tag for clstdicav2  
  - [ ] Italy  Run Italy audit [Janaranjan E](mailto:janaranjan.e@blackstraw.ai)  
  - [ ] 

Jun 22, 2026

- [ ] fluent python fobject and datamodels   
  - [ ] Jump Game  
  - [x] ~~Pascal’s triangle 1~~  
  - [ ] Next Permutation  
  - [ ] Complete data models ch 2   
- [x] ~~Test Census for different clusters~~  
  - [x] ~~see Custom error~~  
  - [x] ~~Hicone fields  germany 2441, bg or bj~~  
- [ ] Hicone explanation   
- [x] ~~**Fix Hicone floating point differences**~~    
  - [x] ~~**Fix for 2438 6B 10701**~~  
  - [x] ~~Fix done , need to check for others pull files , run dict~~  
- [x] ~~**Explain Hiconing and check for hiconed items and see how it is and explain 33792 difference**~~   
  - [x] ~~**Understand Hicone , and how moveunits and movedollars changes  Jun 10, 2026 [SR Vasanthan**](mailto:sr.vasanthan@blackstraw.ai)~~   
- [ ] **What fields get dictionary update**   
- [ ] Learn about cluster, node, spark   
- [ ] wal, context switch  
- [x] ~~SDC  row count mismatch~~  
  - [x] ~~Census  Germany BF, BK, BG, BJ, BE~~  
    - [x] ~~Copy files from tst to dev , trigger dict for all 5 clusters [Janaranjan E](mailto:janaranjan.e@blackstraw.ai)~~  
    - [x] ~~Validate the outputs [Janaranjan E](mailto:janaranjan.e@blackstraw.ai) (move units differing by ± , jana validated it )~~  
    - [ ] 
  - [x] ~~UK  SDC records not found [SR Vasanthan](mailto:sr.vasanthan@blackstraw.ai)~~  
    - [x] ~~Check in~~   
  - [x] ~~4G and 6Z  (Mismatches in Other Streams )~~  
  - [ ] Create automation  
    - [ ] Put In zip , take trends csv file   
    - [ ] Extract the fields with movedollars difference in dictionary   
    - [ ] go and fetch the record from the location , if the field has dictprice , then go and call obtainActPrice  
    - [ ] If no dpo , check hicone field , call obtainActPrice with hicone  
    - [ ] extract the field with moveunits  
    - [ ] check hicone field ,  call obtainActPrice with hicone  
- [ ] Test Audit Jobs  
  - [ ] Germany  77 generate files from Tran , Nagprakash   
    - [ ] week run is 2442, 42, 77, 75 r~~equested files from Nagprakash~~  Nag ditched , requested files from Tran instead  
  - [x] ~~Italy  See Tran message and run it for that file pull 7J files for 2434 or 2438~~  
  - [ ] Re run   
- [ ] 

Jun 15, 2026

- [ ] Manual Procs  
  - [ ] German  Audit Testing   
  - [x] ~~**Test For different week and cluster  2440**~~  
    - [x] ~~**50c35b2e-95a3-4a1a-8d80-3df8938580ee, b38dd1bd-9d19-4c8d-93ab-776325f70b6e**~~  
    - [ ] FOR 77  
  - [x] ~~Tape Job, Tran Mail and do changes~~  
  - [ ] ITADICT  
    - [ ] Test For Cluster 7J  
  - [x] ~~**CENTAPE  Make update as parameter , default is 1**~~  
  - [x] ~~**CENDICT  Make update**~~ `EURO.CENDICT <WEEK>,<CLUSTER>[,CHAIN_LEVEL_IMPUTATION][,QCTYPE][,UPDATE`  
    - [ ] change week, cluster, update   
- [ ] fluent python fobject and datamodels   
  - [x] ~~Set Matrix zeroes~~  
  - [ ] Jump Game   
- [ ] Test Census for different clusters  
  - [ ] see Custom error  
  - [ ] Hicone fields   
- [ ] Fix Hicone floating point differences  
- [ ] **Explain Hiconing and check for hiconed items and see how it is and explain 33792 difference**   
  - [x] ~~**Understand Hicone , and how moveunits and movedollars changes  Jun 10, 2026 [SR Vasanthan**](mailto:sr.vasanthan@blackstraw.ai)~~   
- [ ] **What fields get dictionary update**   
- [ ] Learn about cluster, node, spark   
- [ ] wal

Jun 8, 2026

- [ ] Create a python executable for parsing binary files  
- [ ] **Explain Hiconing and check for hiconed items and see how it is and explain 33792 difference**   
  - [x] ~~**Understand Hicone , and how moveunits and movedollars changes  Jun 10, 2026 [SR Vasanthan**](mailto:sr.vasanthan@blackstraw.ai)~~   
  - [ ] **What fields get dictionary update**   
- [ ] Learn about cluster, node, spark   
- [ ] wal  
- [ ] **fluent python fobject and datamodels**   
- [ ] Merge sort, time complexities, Two pointer  
- [ ] Manual Procs  
  - [ ] Audit  German   
    - [ ] Test For different week and cluster  
- [ ] Test Census for different clusters  
  - [ ] see Custom error  
  - [ ] Hicone fields   
- [x] ~~Create automation for data validation~~  
  - [x] ~~utils  obtainactPrice.py Jun 10, 2026 [SR Vasanthan](mailto:sr.vasanthan@blackstraw.ai)~~  
  - [x] ~~Do it for2440, UK clusters~~  
  - [x] ~~NON-DCS 2I~~  
  - [x] ~~DCS 32~~   
- [x] ~~Read the chapter~~   
- [ ] Create a simple database with lsm and b tree



May 28, 2026  Jun 1, 2026  Jun 5, 2026

- [ ] Create a python executable for parsing binary files  
- [x] ~~Make CENDICT PART2   [Janaranjan E](mailto:janaranjan.e@blackstraw.ai)~~  
  - [x] ~~/gr/causal/output/week  ascii file 1~~   
  - [x] ~~/gr/causal/ICAAUDIT/week  binary file 2~~  
- [x] ~~**DICTWK2  main dict read script  hicone logging 2 fields missing**   [SR Vasanthan](mailto:sr.vasanthan@blackstraw.ai)~~  
- [x] ~~Handle Custom Error in CENDICT part 1 [SR Vasanthan](mailto:sr.vasanthan@blackstraw.ai)~~  
- [x] ~~Triggering Utility in audfrma, clstdica, clstmova , [SR Vasanthan](mailto:sr.vasanthan@blackstraw.ai)~~  
- [x] ~~ITADICT  [SR Vasanthan](mailto:sr.vasanthan@blackstraw.ai)~~  
- [x] ~~**Validation check , John and Kiran for clusters** [SR Vasanthan](mailto:sr.vasanthan@blackstraw.ai)~~  
- [x] ~~**Put a mail for FRN files**~~  
- [ ] **Explain Hiconing and check for hiconed items and see how it is and explain 33792 difference**  
- [ ] Understand Hicone , and how moveunits and movedollars changes   
  - [ ] Handle Error, trigger IS util like system unavailable  
- [x] ~~Go through sysprint logs~~  
- [ ] Learn about cluster, node, spark   
- [ ] Merge sort, time complexities  
- [ ] Manual Procs  
  - [x] ~~CENMERGE (Done and Dusted, but didnt tested till load job )~~  
  - [ ] **FRNBATCH**   
    - [x] ~~**Trigger again and with comma**~~   
    - [x] ~~**with two weeks**~~  
    - [x] ~~**Include UPDATE parameter , it is defaulted to zero**~~   
    - [ ] **Try it for FRN chain**  
  - [ ] AUDFRMA    
    - [x] ~~Ask libin for what change has been happened for hyphen for ALPHADESCR , incorporate those changes in the flow~~  
    - [x] ~~Sysprint logs~~   
  - [ ] **CLSTDICA**  
    - [x] ~~**Run clstdica in design mode and along with test harness flow**~~   
    - [x] ~~Check 409 mismatches and query no of distinct stores~~  
  - [ ] **CLSTMOVA**   
    - [x] ~~Need to change output files format~~   
    - [x] ~~What is INFO.MOVEMENT   ask roopasree~~  
    - [x] ~~Fix order in output file~~  
    - [x] ~~Fix mismatches~~  
      - [x] ~~Convert weekdata.e42 to df~~  
      - [x] ~~Thiripi run in design mode for weekmove , check both counts~~  
      - [x] ~~run in design mode, check for logs~~  
      - [x] ~~Solve mismatches~~  
      - [x] ~~Run for e77 , weekdata  1003428~~  
      - [x] ~~parse weekmove file and get counts~~  
      - [x] ~~Build a miniature version of harness which just provide column wise stats and joins upc and store number~~  
      - [x] ~~Parse BASEOUT and match th~~
  - [ ] **ITADICT**  
- [ ] Fix **FAKCOUNT**  
- [x] ~~**Re Run for 51656 51757 **~~    
  - [x] ~~Insert mf Dictionary Values with any of our backups~~  
    - [x] ~~Get necessary fields from Dictionary used in DICTWK2~~  
    - [x] ~~Update main table~~   
  - [x] ~~Test mf Dictionary values with updated pg tables~~  
  - [x] ~~Run and Test~~

May 18, 2026

- [x] ~~Include delimiter parameter in aproc~~  
  - [x] ~~cendict, cenmove, [cenmerge](),~~   
- [ ] **Change LETTPC, SYSRPT from root**  
- [x] ~~Add sysprint header in all scripts | fix upc formatting~~  
- [ ] Manual Procs  
  - [ ] CENMERGE  
    - [x] ~~Test with Dictionary change, dbhost, etc~~  
    - [x] ~~Include dictdbhost, dictdbport, storedbhost~~  
  - [ ] FRNBATCH  
    - [ ] Trigger again  
    - [x] ~~Include UPDATE parameter~~   
  - [ ] AUDFRMA    
    - [x] ~~**Run audfrma, do test harness**~~   
    - [ ] Ask libin for what change has been happened for hyphen for ALPHADESCR , incorporate those changes in the flow  
    - [ ] Sysprint logs   
    - [x] ~~Fix STORTYPE~~   
  - [x] ~~**CLSTDICA**~~  
    - [x] ~~**Run Clstdica do test harness**~~  
    - [x] ~~Test Dictionary~~  
    - [ ] Run clstdica in design mode and along with test harness flow  
    - [ ] Check 409 mismatches and query no of distinct stores  
  - [ ] **CLSTMOVA**  
    - [x] ~~Need to change output files format~~   
    - [ ] What is INFO.MOVEMENT   ask roopasree  
    - [ ] sysprint logs  
  - [ ] **ITADICT**  
  - [ ] Understand Hicone , and how moveunits and movedollars changes   
  - [x] ~~Complete Test harness  (Done as TestHarnesser)~~  
  - [ ] Handle Error, trigger IS util like system unavailable   
- [ ] Fix **FAKCOUNT**  
- [x] ~~**See WEEKMOVE chain ID**~~  
- [ ] Re Run for 51656 51757  
  - [ ] Insert mf Dictionary Values with any of our backups  
    - [x] ~~Get necessary fields from Dictionary used in DICTWK2~~  
    - [x] ~~Update main table~~   
    - [ ] ~~Update tall tables separately~~   
  - [ ] Test mf Dictionary values with updated pg tables  
  - [x] ~~Get files from Roopa~~  
  - [ ] Run and Test  
- [ ] 33792 Records mismatches

May 11, 2026

- [ ] Include delimiter parameter in aproc  
- [x] ~~why exploding takes time  Sysprint Logs~~   
- [ ] **Change LETTPC, SYSRPT**  
- [x] ~~Test Dictionary DB~~  
- [x] ~~Read 5 pages of DDIA~~  
- [x] ~~Do the changes to dev~~   
- [ ] Solve 1 two pointer   
- [ ] Manual Procs  
  - [ ] CENMERGE  
    - [ ] Test with Dictionary change, dbhost, etc  
  - [ ] FRNBATCH  
    - [ ] Trigger again  
  - [x] ~~EANAUDA~~  
    - [ ] Ask roop on the different location of the files  
  - [ ] AUDFRMA    
    - [x] ~~call nagprakash on this~~  
    - [ ] **Run audfrma, do test harness**   
    - [ ] Ask libin for what change has been happened for hyphen for ALPHADESCR , incorporate those changes in the flow  
- [ ] **CLSTDICA**  
  - [x] ~~Add SYSPRINT LOGS, stats, NewItemFile Creation~~  
    - [x] ~~mdbpkyc4~~  
    - [x] ~~mdbpwkad~~  
  - [x] ~~execution context, processingtype~~  
  - [ ] **Run Clstdica do test harness**  
  - [ ] Test Dictionary  
- [ ] **CLSTMOVA**  
- [ ] **ITADICT**  
- [ ] Understand Hicone , and how moveunits and movedollars changes   
- [ ] Complete Test harness  
- [ ] Handle Error, trigger IS util like system unavailable   
- [ ] Fix **FAKCOUNT**  
- [x] ~~Fix test harness logic for dict~~ 

May 4, 2026

- [ ] Include delimiter parameter in aproc  
- [ ] why exploding takes time  
- [x] ~~Description~~  
- [x] ~~Dictionary Match~~  
  - [x] ~~WLM~~  
  - [x] ~~**Description**~~  
- [ ] Manual Procs  
  - [ ] CENMERGE  
    - [ ] Test with Dictionary change, dbhost, etc  
  - [ ] FRNBATCH  
    - [ ] Trigger again  
  - [ ] AUDFRMA    
    - [ ] call nagprakash on this  
- [ ] 
- [ ] **CLSTDICA**  
  - [ ] Add SYSPRINT LOGS, stats, NewItemFile Creation  
  - [ ] execution context, processingtype  
  - [x] ~~**Implement Batch Updates**~~   
    - [x] ~~get keycat sql table~~   
    - [x] ~~MDBPKYC4~~   
    - [x] ~~put table name in config~~  
    - [x] ~~MDBPWKAD~~  
  - [ ] Test Dictionary  
  - [x] ~~Add DICTWK2 snippet~~  
  - [ ] Change to starndardized parameters  
- [ ] **CLSTMOVA**  
  - [ ] **Test Move**  
  - [ ] Add sysprint logs  
  - [ ] Use nfs  
- [ ] **ITADICT**  
  - [x] ~~**Extract JCL from Tran**~~  
- [ ] ~~**ITATAPE**~~  
  - [x] ~~**Extract JCL from Tran**~~  
- [x] ~~Remove Abbreviation logic~~   
  - [x] ~~| — hyphen~~  
  - [x] ~~Removing leading and trailing spaces~~  
  - [ ] 

Apr 20, 2026

- [x] ~~Debug DICTPRICE / MOVEDOLLARS issue~~  
  - [x] ~~add debug statements in dictwk2~~  
- [x] ~~Understand what is price override, dynamic price override, hicone price~~   
- [ ] Fix log   
- [ ] Include delimiter parameter in aproc  
- [ ] Dictionary Match  
  - [ ] WLM  
  - [ ] **Description**  
  - [x] ~~**KEYCAT**~~  
- [ ] Manual Procs  
  - [ ] CENMERGE  
    - [ ] Test with Dictionary change, dbhost, etc  
  - [ ] FRNBATCH  
    - [ ] Trigger again  
  - [ ] AUDFRMA    
    - [ ] call nagprakash on this  
    - [x] ~~change greancnv to audfrma~~  
    - [ ] Minor changes use nfs   
    - [ ] Fix comma arguments  
    - [ ] use config  
    - [x] ~~Run using test harness for all three clusters~~  
  - [ ] **CLSTDICA**  
    - [ ] **Implement Batch Updates**   
    - [ ] Test Dictionary  
    - [ ] Add DICTWK2 snippet  
  - [ ] **CLSTMOVA**  
    - [ ] **Test Move**  
  - [ ] **ITADICT**  
    - [ ] **Extract JCL from Tran**  
  - [ ] **ITATAPE**  
    - [ ] **Extract JCL from Tran**



Apr 13, 2026

- [ ] Learn Networking, debugging  
- [x] ~~**Simulate dictionary by empty db and see what the output is**~~   
  - [x] ~~**Test with abbreviations, understand that dictwk2**~~    
  - [x] ~~Test for hiconelogic, Give step by step to cursor and it to docs  etlflow analysis Apr 10, 2026~~  
- [x] ~~Stat reports, sysprint report going in census~~  
  - [x] ~~**After done update it with commands [Train**](https://iriworldwide.sharepoint.com/:x:/r/sites/grp-O365-EMEA-Data-Loading/_layouts/15/Doc.aspx?sourcedoc=%7B5AEBFD9C-979A-4610-B8B2-46B10ACFED30%7D&file=UK_Train_Schedule_UAT%20Tracker.xlsx&action=default&mobileredirect=true)~~  
- [x] ~~**Dictionary Description**~~   
  - [x] ~~**Trim Spaces**~~  
  - [x] ~~**add hiconefactor , and test with**~~   
- [ ] **Complete CLSTDICA this week**  
- [ ] **Test for AUDFRMA  Apr 10, 2026**  
- [ ] CENMERGE  
  - [ ] Test with Dictionary change, dbhost, etc  
- [ ] FRNBATCH  
  - [ ] Trigger again  
- [ ] AUDFRMA    
  - [ ] call nagprakash on this  
  - [ ] change greancnv to audfrma  
  - [ ] Minor changes use nfs   
- [ ] **CLSTDICA**  
  - [ ] **Implement Batch Updates**   
  - [ ] Test Dictionary  
  - [ ] Add DICTWK2 snippet  
- [ ] **CLSTMOVA**  
  - [ ] **Test Move**  
- [ ] **ITADICT**  
  - [ ] **Extract JCL from Tran**  
- [ ] **ITATAPE**  
  - [ ] **Extract JCL from Tran**

Apr 5, 2026

- [ ] Learn Networking, debugging  
- [ ] Aproc  Apr 10, 2026  
  - [x] ~~Run UKFEAT~~  
  - [x] ~~Run TAPE, DICT~~  
  - [x] ~~Run Move, EURO.TAPE~~  
- [x] ~~Dictionary Issue     Apr 9, 2026~~  
- [x] ~~Test harness   Apr 9, 2026 by Jana~~  
- [x] ~~Deep Dive Email , MIME, POP etc~~  
- [ ] **Simulate dictionary by empty db and see what the output is**   
  - [ ] **Test with abbreviations, understand that dictwk2**    
  - [ ] Test for hiconelogic, Give step by step to cursor and it to docs  etlflow analysis Apr 10, 2026  
  - [x] ~~UAT  50935, 50957  Store Trigger dictionary~~  
- [ ] CENMERGE  
  - [ ] Test with Dictionary change, dbhost, etc  
- [ ] FRNBATCH  
  - [ ] Trigger again  
- [ ] AUDFRMA    
  - [ ] call nagprakash on this  
  - [ ] change greancnv to audfrma  
  - [ ] Minor changes use nfs   
- [ ] **CLSTDICA**  
  - [ ] **Implement Batch Updates**   
  - [ ] Test Dictionary  
  - [ ] Add DICTWK2 snippet  
- [ ] **CLSTMOVA**  
  - [ ] **Test Move**  
- [ ] **ITADICT**  
  - [ ] **Extract JCL from Tran**  
- [ ] **ITATAPE**  
  - [ ] **Extract JCL from Tran**

Mar 30, 2026  Apr 2, 2026

- [x] ~~Consolidate server information along with canonical and hostnames~~  
- [x] ~~Learn Pdb~~  
- [x] ~~Learn Pandas , Numpy~~  
- [ ] Learn Networking, debugging   
- [x] ~~Customize Pdb~~  
- [x] ~~test the above in aproc~~  
  - [x] ~~EURO.TAPE~~  
  - [x] ~~EANAUDA~~  
- [x]  ~~**Credential changes**~~   
  - [x] ~~Alter CENDICTPART1 Flow to incorporate parameters DICT,STOREDB also make documentation~~

```
DICT_DB_HOST
DICT_DB_NAME DATABASE_NAME
DICT_DB_USER
DICT_DB_PASS
DICT_DB_PORT

STORE_DB_HOST
STORE_DB_NAME STORE_DB
STORE_DB_USER
STORE_DB_PASS
STORE_DB_PORT

```

- [x] ~~Alter Snippet , incorporate DICT, STOREDB parameters make documentation~~   
- [x] ~~Test Run it for GX,~~   
- [x] ~~Ask Vijay bro to do the same changes as following~~   
- [ ] **Talk with dictionary**  [RE: Spain  DL  Dictionary updates testing/validation](https://mail.google.com/mail/#search/rfc822msgid%3A%3Cairmail-4907bbe7-888a-4621-b64c-81fa4a6da5d7%40google.com%3E?oor=true)  
  - [ ] **Test with abbreviations, understand that dictwk2**    
- [ ] **Simulate dictionary by empty db and see what the output is**   
  - [x] ~~Now delete the data and try~~   
  - [x] ~~some steps~~   
  - [ ] Test for Log creating scenarios   
- [x] ~~EURO.TAPE~~    
  - [x] ~~Connect with aashika , regarding the new parameters~~
    ```
    chain \- BTS

    week \- 2419

    USE\_FTP\_FOR\_IS\_FS \- NO

    country \- CC  
    country-code \- C

    is\_snippet\_upgrade\_check \- default true

    Store\_N \- 64886

    testmode \- default 1 | 0

    env \- dev

    content\_name \- eudl\_publish\_config

    tenant \- CL1
    ```

- [ ] CENMERGE  
  - [x] ~~**Ask rajes about three approaches**~~  
- [ ] FRNBATCH  
  - [ ] Trigger again  
- [ ] AUDFRMA    
  - [x] ~~Test it from eanauda triggering~~   
  - [ ] call nagprakash on this  
  - [ ] change greancnv to audfrma  
- [ ] **CLSTDICA**  
  - [ ] **Implement Batch Updates**   
  - [ ] Test Dictionary  
  - [ ] Add DICTWK2 snippet  
- [ ] **CLSTMOVA**  
  - [ ] **Test Move**  
- [x] ~~UI.SMPITAH~~  
  - [x] ~~Analyze what is ui, i/p, process~~    
  - [x] ~~analyze sarayu code, hadoop~~  
  - [x] ~~analyze aproc hadoop how it is different~~   
  - [x] ~~hadoop ui~~   
  - [x] ~~and just extract with sample data~~  
- [x] ~~UI.SCAWCNEH~~  
  - [x] ~~Analyze what it ui, i/p, process~~  
- [ ] **ITADICT**  
  - [ ] **Extract JCL from Tran**  
- [ ] **ITATAPE**  
  - [ ] **Extract JCL from Tran**

Mar 25, 2026

- [ ] test the above in aproc  
  - [ ] EURO.TAPE  
  - [ ] EANAUDA  
- [x] ~~Change SYSPRINT, SYSRPT to incorporate sample , SENDLETT3 not workin~~  
  - [x] ~~writelettpc is defined as writelettpc(logpath, week, message) but called as writelettpc(logpath, WEEK, msg, Inputs) (extra arg)~~  
  - [x] ~~creating not under sample~~  
  - [x] ~~DICTwrites being empty~~  
- [x] ~~Add Comment~~  
- [ ] **Simulate dictionary by empty db and see what the output is**   
  - [x] ~~See what field dictionary is affecting , including iritem fields~~  
- [ ] **NEWPROC:**  
  - [ ] EURO.TAPE    
  - [ ] CENMERGE  
    - [x] ~~Call CENMERGE Flow from Tape Job~~  
    - [x] ~~Call Dict from CENMERGE Flow~~  
  - [ ] AUDFRMA    
    - [ ] Test it from eanauda triggering   
    - [ ] call nagprakash on this  
    - [ ] change greancnv to audfrma  
  - [ ] **CLSTDICA**  
    - [ ] **Implement Batch Updates**   
    - [ ] Test Dictionary  
    - [ ] Add DICTWK2 snippet  
  - [ ] **CLSTMOVA**  
    - [ ] **Test Move**  
  - [ ] UI.SMPITAH  
    - [ ] Analyze what is ui, i/p, process  
    - [ ] Analyze what is   
  - [ ] UI.SCAWCNEH  
    - [ ] Analyze what it ui, i/p, process  
  - [ ] ITADICT  
    - [x] ~~Consult with GOC / Rajesh audit~~   
    - [x] ~~Kiran will answer~~  
  - [ ] ITATAPE  
    - [x] ~~Consult with GOC / Rajesh Audit~~  
    - [x] ~~Kiran will answer~~

Mar 17, 2026

- [ ] test the above in aproc  
  - [ ] EURO.TAPE  
  - [ ] EANAUDA  
- [ ] Add Comments   
- [x] ~~DIC ISSUE~~    
  - [x] ~~re run it using mainframe file~~  
  - [x] 
- [ ] **Simulate dictionary by empty db and see what the output is**   
- [ ] **NEWPROC:**  
  - [ ] EURO.TAPE    
  - [ ] CENMERGE  
    - [ ] Call CENMERGE Flow from Tape Job  
    - [ ] Call Dict from CENMERGE Flow  
    - [ ] Call   
  - [ ] AUDFRMA    
    - [ ] Test it from eanauda triggering   
    - [ ] call nagprakash on this  
    - [ ] change greancnv to audfrma  
  - [ ] **CLSTDICA**  
    - [ ] **Implement Batch Updates**   
    - [ ] Test Dictionary  
    - [ ] Add DICTWK2 snippet  
  - [ ] **CLSTMOVA**  
    - [ ] **Test Move**



Mar 16, 2026

- [x] ~~TRANS2U~~   
  - [x] ~~Tell nagprakash that erc7 files are not there for 2419 to 2427 but it was present in 2392~~  
  - [x] ~~rc7 is mcc chain belongs to 2U cluster and a part of RWC~~

- [x] ~~EANAUDA~~  
  - [ ] 

~~UKFEAT~~  
~~HOLFEAT~~  
~~DIC DE  holland Issue~~

- [ ] re run it using mainframe file raw Mar 17, 2026

FRNBATCH

- [x] ~~EURO.TAPE  call aashika or vijay tomorrow morning ⌛~~

- [ ] test the above in aproc  Mar 17, 2026  
- [ ] push clstdica, clstmova, audfrma in aproc

Mar 5, 2026

- [ ] Italy time taking  
  - [ ] modify dict to make it batch reads and batch updates  
    - [ ] from psycopg2.extras import executebatch  
- [ ] Add Comments   
  - [ ] de, dic ISSUE  
- [x] ~~Fix snippet issue~~  
- [ ] Simulate dictionary by empty db and see what the output is   
- [ ] Sample dict flow  log save  
- [x] ~~Use raise error, with iritem, Dict~~   
- [x] ~~Talk with shreyansh , the cli arguments [SR Vasanthan](mailto:sr.vasanthan@blackstraw.ai)~~   
- [ ] **NEWPROC:**  
  - [x] ~~Create a audit config, place flow ids, db details there~~  
  - [x] ~~**CENDICT**~~  
  - [x] ~~**CENMOVE**~~  
  - [x] ~~**CENTAPE**~~  
  - [x] ~~**EURO.TAPE**~~  
  - [x] ~~**FEAT PROCS**~~  
    - [x] ~~**EURO.SPFEAT**~~  
    - [x] ~~**EURO.FRFEAT**~~  
    - [x] ~~**EURO.GRFEAT**~~  
    - [x] ~~**FIELD.ITFEA**~~  
    - [x] ~~**HOFEAT**~~  
    - [x] ~~**UKFEAT**~~  
  - [ ] **CENMERGE**  
    - [ ] **Call CENMERGE Flow from Tape Job**  
  - [x] ~~**FRNBATCH**~~  
    - [x] ~~**Manipulate the Existing Flow**~~   
  - [x] ~~**EANAUDA**~~  
    - [x] ~~**Modify the proc with darshan code**~~   
    - [x] ~~Test in new aproc server~~   
  - [x] ~~**EAUDFRMA**~~  
    - [x] ~~get Input from /raw when vpn access~~  
    - [x] ~~Add Configs~~  
  - [ ] **CLSTDICA**  
    - [ ] **Implement proc that will tell us the payload**  
    - [x] ~~Add Configs~~  
    - [ ] Implement Standardization file path   
    - [x] ~~Create a Master Flow which will have dictionary job has Snippet~~  
    - [ ] **Implement Batch Updates**   
    - [ ] ~~Implement Flow Control~~  
      - [ ] ~~Country based Logics~~  
    - [x] ~~After that implement MDWK / MDYAD in a script level~~  
    - [x] ~~Integrate all into single flowa~~  
    - [ ] Test Dictionary  
    - [x] ~~Add DICTWK2 snippet~~  
      - [ ] Starter  
      - [ ] Connection   
        - [ ] NEWITEM  
        - [ ] WEEKDATA  
  - [x] ~~**CLSTMOVA**~~  
    - [x] ~~Add Configs~~  
    - [x] ~~Implement~~   
    - [x] ~~Implement Standardization file path~~   
    - [ ] **Test Move**

Feb 23, 2026  Feb 27, 2026

- [x] ~~Records removed deleted  2422CUOT7~~  
- [x] ~~Implement NFS changes~~  
  - [x] ~~Phase 1 ( Fixer, Validate, validatePreDict)~~  
  - [x] ~~Phase 2 (MainDictRead, Keycat)~~  
  - [x] ~~Phase 3 ( Consolidate, Newitem )~~  
    - [x] ~~Create a dummy sysprint file which states the program name at the end of snippet~~   
    - [x] ~~Tag changes~~  
- [x] ~~Trigger again and see~~  
- [ ] France, Italy exceeding  
  - [ ] modify dict to make it batch reads and batch updates  
    - [ ] from psycopg2.extras import executebatch  
- [ ] **NEWPROC:**  
  - [ ] Create a audit config, place flow ids, db details there   
  - [ ] **CENMERGE**  
    - [ ] **Call CENMERGE Flow from Tape Job**  
  - [ ] **FRNBATCH**  
    - [ ] Manipulate the Existing Flow   
  - [ ] **EANAUDA**  
    - [ ] **Modify the proc with darshan code**   
    - [ ] Test in new aproc server   
  - [ ] **EAUDFRMA**  
    - [ ] get Input from /raw when vpn access  
    - [ ] Add Configs  
  - [ ] **CLSTDICA**  
    - [ ] **Implement proc that will tell us the payload**  
    - [ ] Add Configs  
    - [ ] Implement Standardization file path   
    - [ ] Create a Master Flow which will have dictionary job has Snippet  
    - [ ] **Implement Batch Updates**   
    - [ ] Implement Flow Control  
      - [ ] Country based Logics  
    - [x] ~~After that implement MDWK / MDYAD in a script level~~  
    - [ ] Integrate all into single flowa  
    - [ ] Test Dictionary  
    - [ ] Add DICTWK2 snippet  
      - [ ] Starter  
      - [ ] Connection   
        - [ ] NEWITEM  
        - [ ] WEEKDATA  
  - [x] ~~**CLSTMOVA**~~  
    - [x] ~~Get JCL, Input dataframe~~  
    - [x] ~~Alter the flow , incorporate basic template , audparm reading etc~~  
    - [ ] Add Configs  
    - [ ] Implement   
    - [ ] Implement Standardization file path   
    - [x] ~~Implement Flow Control~~  
    - [x] ~~Analyze it~~   
      - [x] ~~qcdiv~~  
      - [x] ~~plclustmov~~  
    - [x] ~~Implement~~  
      - [x] ~~**qcdiv**~~  
      - [x] ~~plclustmov~~  
    - [ ] **Test Move**

Feb 16, 2026   Feb 20, 2026

- [ ] Logging  
  - [x] ~~Check for all countries~~  
- [ ] France, Italy exceeding  1 hr  
  - [x] ~~Modify dict update query or~~  
  - [ ] modify dict to make it batch reads and batch updates  
  - [ ] from psycopg2.extras import executebatch  
  - [ ] ~~**Action plan**~~   
    - [ ] ~~Backup db~~   
    - [x] ~~Create stats for other countries~~  
    - [x] ~~see explain analyze and compare the results with and use cursor~~   
  - [ ] Learn from Ultimatum   
- [ ] **NEWPROC:**  
  - [ ] Create a audit config, place flow ids, db details there   
  - [ ] **CENMERGE**  
    - [ ] **Call CENMERGE Flow from Tape Job**  
  - [ ] **FRNBATCH**  
    - [ ] Manipulate the Existing Flow   
  - [x] ~~**EANAUDA**~~  
    - [ ] Test in new aproc server   
  - [ ] **EAUDFRMA**  
    - [ ] get Input from /raw when vpn access  
    - [ ] Add Configs  
  - [ ] **CLSTDICA**  
    - [ ] Add Configs  
    - [ ] Implement Standardization file path   
    - [ ] Create a Master Flow which will have dictionary job has Snippet  
    - [ ] Implement Batch Updates   
    - [ ] Implement Flow Control  
      - [ ] Country based Logics  
    - [x] ~~After that implement MDWK / MDYAD in a script level~~  
    - [ ] Integrate all into single flowa  
    - [ ] Test  
    - [ ] Add DICTWK2 snippet  
  - [ ] **CLSTMOVA**  
    - [ ] Alter the flow , incorporate basic template , audparm reading etc  
    - [ ] Add Configs  
    - [ ] Implement Standardization file path   
    - [ ] Implement Batch Updates   
    - [ ] Implement Flow Control  
    - [ ] Analyze it   
      - [x] ~~qcdiv~~  
      - [ ] plclustmov  
    - [ ] Implement  
      - [ ] **qcdiv**  
      - [ ] plclustmov

Feb 10, 2026  Feb 13, 2026

- [ ] Logging  
  - [ ] Check for all countries  
    - [x] ~~logs creating in uk directory~~   
  - [x] ~~Ensure the logs are created with idempotent~~  
  - [x] ~~Include PROCESSINGTYPE in the log directory~~  
  - [x] ~~Remove unwanted parameters from Snippet~~  
    - [x] ~~isStandalone~~  
  - [x] ~~Add the following in the docs~~  
- [ ] France, Italy exceeding  1 hr  
  - [ ] ~~Take UK, France, Italy weekdata raw and just include it in the script including the rdd mapPartition~~   
  - [ ] ~~Rate the performance for the all three~~  
  - [ ] Modify the query, modify the index   
  - [x] ~~**edit main dict read with notebook 46 and validatepredict notebook 47**~~  
  - [x] ~~DictObj bug~~  
  - [x] ~~str() to int()~~  
  - [ ] test batch mode reads  
    - [ ] from psycopg2.extras import executebatch  
  - [ ] 
- [x] ~~Deep dive why IS triggering works , work in the local device and see it in postman ~~   
- [x] ~~Test with devs~~  
  - [x] ~~NSLQC~~  
  - [ ] WEEKMOVE  
  - [x] ~~BATDICT~~  
- [ ] **NEWPROC:**  
  - [ ] Create a audit config, place flow ids, db details there   
  - [ ] Check ,   
  - [ ] **CENMERGE**  
    - [ ] **Call CENMERGE Flow from Tape Job**  
    - [x] ~~Use existing script ,~~   
    - [x] ~~push in svn~~  
  - [ ] **FRNBATCH**  
    - [ ] Manipulate the Existing Flow   
  - [x] ~~**EANAUDA**~~  
    - [ ] Test in new aproc server   
  - [ ] **EAUDFRMA**  
    - [ ] get Input from /raw when vpn access  
    - [ ] Add Configs  
  - [ ] **CLSTDICA**  
    - [ ] Add Configs  
    - [ ] Implement Standardization file path   
    - [ ] Create a Master Flow which will have dictionary job has Snippet  
    - [ ] Implement Batch Updates   
    - [ ] Implement Flow Control  
      - [ ] Country based Logics  
    - [x] ~~After that implement MDWK / MDYAD in a script level~~  
    - [ ] Integrate all into single flowa  
    - [ ] Test  
  - [ ] **CLSTMOVA**  
    - [ ] Add Configs  
    - [ ] Implement Standardization file path   
    - [ ] Implement Batch Updates   
    - [ ] Implement Flow Control  
    - [ ] Analyze it   
      - [ ] qcdiv  
      - [ ] plclustmov  
    - [ ] Implement  
      - [ ] qcdiv  
      - [ ] plclustmov



Feb 3, 2026  Feb 6, 2026

- [ ] Logging  
  - [x] ~~STAT~~  
  - [x] ~~SYSPRINT~~  
    - [x] ~~Add SYSPRINT Logger in False block~~   
    - [x] ~~Add field logmessage, logtype  SYSRPT, SYSPRINT~~  
    - [x] ~~Remove the unnecessary parameters and refactor the components~~  
      - [ ] take backup  
  - [x] ~~LETTPC~~  
  - [x] ~~LETTPR~~  
  - [x] ~~SYSPRPT~~  
  - [x] ~~SYSLOG~~  
- [x] ~~**DICTWK2 as Snippet**  Re Designing and separating our all the components and concers~~  
  - [x] ~~Complete New Item~~  
  - [x] ~~Complete consolidated to WKBCM2, triggerMove~~  
- [ ] Complete DICTWK2 Snippet document   
- [x] ~~Edit icuat api triggering~~   
- [x] ~~do the changes in higher env~~  
- [x] ~~part2 not triggering~~  
- [ ] deep dive why the is trigger is working  
- [ ] France, Italy exceeding  1 hr   
- [x] ~~IS triggers~~  
  - [x] ~~BATDICT~~  
  - [x] ~~NSLQC~~  
  - [x] ~~WEEKMOVE~~

Jan 16, 2026

- [x] ~~**DICTWK2 as Snippet**  Re Designing and separating our all the components and concers~~  
  - [x] ~~edit snippet~~  
  - [x] ~~get Input form the flow and use it as snippet~~   
  - [x] ~~go to notebook and run it from inside~~  
- [x] ~~python aproc~~  
  - [x] ~~dto for is triggering~~  
  - [ ] config location for file path resolver  
- [ ] **France taking 1hr  for dict **   
  - [ ] happening only if dictionary is updated by ours   
- [ ] **add Comb and is standalone logic for wkbcm2**  
- [x] ~~Fix Dictionary fields correctly , check one by one and its fields and make sure it never fails~~   
- [x] ~~**Add SYSLOG**~~  
  - [x] ~~look into logging~~  
  - [x] ~~MANAGE SYSPRINT,~~   
- [ ] **Main Flow Triggering Utility**   
- [ ] **NEWPROC:**  
  - [ ] **CENMERGE**  
    - [ ] **Call CENMERGE Flow from Tape Job**  
    - [x] ~~Use existing script ,~~   
    - [x] ~~push in svn~~  
  - [ ] **CPYFKPYT**   
    - [ ] Analyze Basic I/O Processing   
    - [ ] Analyze the Python Program  
    - [ ] Analyze How Parsing Works  
  - [ ] **FRNBATCH**  
    - [ ] Manipulate the Existing Flow   
  - [x] ~~**EANAUDA**~~  
    - [ ] Test in new aproc server   
  - [ ] **EAUDFRMA**  
    - [ ] get Input from /raw when vpn access  
    - [ ] Add Configs  
  - [ ] **CLSTDICA**  
    - [ ] Add Configs  
    - [ ] Implement Standardization file path   
    - [ ] Create a Master Flow which will have dictionary job has Snippet  
    - [ ] Implement Batch Updates   
    - [ ] Implement Flow Control  
      - [ ] Country based Logics  
    - [x] ~~After that implement MDWK / MDYAD in a script level~~  
    - [ ] Integrate all into single flowa  
    - [ ] Test  
  - [ ] **CLSTMOVA**  
    - [ ] Add Configs  
    - [ ] Implement Standardization file path   
    - [ ] Implement Batch Updates   
    - [ ] Implement Flow Control  
    - [ ] Analyze it   
      - [ ] qcdiv  
      - [ ] plclustmov  
    - [ ] Implement  
      - [ ] qcdiv  
      - [ ] plclustmov  
- [ ] 

Jan 12, 2026

- [ ] **France taking 1hr  for dict **   
- [x] ~~**copy changes to cendict **~~   
- [ ] **add Comb and is standalone logic for wkbcm2**  
- [x] ~~**SAVEDOLLARS **~~   
- [x] ~~***WKBKCM2**  EXCEPT UK *~~   
  - [x] ~~*Try it with cursor, explore*~~  
- [x] ~~**EUROSCAN.BPPR**  Change that to actual file~~  
- [ ] Fix Dictionary fields correctly , check one by one and its fields and make sure it never fails 

- [ ] .destroy() broadcast variables used in dict flow  
- [x] ~~Clean up Script~~   
  - [x] ~~Backup File~~  
  - [x] ~~Delete~~   
- [ ] **Create a df where the discarded records are left and given a reason for the discard**   
- [ ] **Need to implement part before READNEXT  invalid generation**

**Jan 5, 2026**

- [ ] Learn file manipulation with python and bash  
- [ ] ***WKBKCM2**  EXCEPT UK *   
  - [ ] *Try it with cursor, explore*  
- [ ] **EUROSCAN.BPPR**  Change that to actual file  
- [ ] **NEWPROC:**  
  - [ ] **CPYFKPYT**   
    - [ ] Analyze Basic I/O Processing   
    - [ ] Analyze the Python Program  
    - [ ] Analyze How Parsing Works  
  - [ ] **FRNBATCH**  
    - [ ] Manipulate the Existing Flow   
  - [x] ~~**EANAUDA**~~  
    - [ ] Change to /raw when vpn access  
  - [ ] **EAUDFRMA**  
    - [ ] get Input from /raw when vpn access  
    - [ ] Add Configs  
  - [ ] **CLSTDICA**  
    - [ ] Add Configs  
    - [ ] Implement Standardization file path   
    - [ ] Create a Master Flow which will have dictionary job has Snippet  
    - [ ] Implement Batch Updates   
    - [ ] Implement Flow Control  
      - [ ] Country based Logics  
    - [x] ~~DO for Cluster 75~~  
      - [x] ~~raw to df~~  
      - [x] ~~run eaudfrma~~  
      - [x] ~~run clstdica~~   
    - [ ] After that implement MDWK / MDYAD in a script level  
      - [x] ~~MDWK~~  
        - [ ] implement last batch updates  
      - [x] ~~MDYAD~~  
        - [x] ~~Analyze it~~   
        - [x] ~~show the mdwk and implement like ths~~  
    - [ ] Integrate all into single flow  
    - [ ] Test  
  - [ ] **CLSTMOVA**  
    - [ ] Add Configs  
    - [ ] Implement Standardization file path   
    - [ ] Implement Batch Updates   
    - [ ] Implement Flow Control  
    - [ ] Analyze it   
      - [ ] qcdiv  
      - [ ] plclustmov  
    - [ ] Implement  
      - [ ] qcdiv  
      - [ ] plclustmov  
    - [ ] 

**Dec 22, 2025**

- [ ] Learn file manipulation with python and bash  
- [ ] ***WKBKCM2**  EXCEPT UK *   
  - [ ] *Try it with cursor, explore*  
- [ ] **NEWPROC:**  
  - [ ] Need JCL for Audit Programs  
  - [ ] Input Files for the above  
  - [ ] **CPYFKPYT**   
    - [ ] Analyze Basic I/O Processing   
    - [ ] Analyze the Python Program  
    - [ ] Analyze How Parsing Works  
  - [ ] **FRNBATCH**  
  - [x] ~~**EANAUDA**~~  
    - [ ] Change to /raw when vpn access  
  - [ ] **EAUDFRMA**  
    - [ ] get Input from /raw when vpn access  
    - [x] ~~Analyze PL~~  
    - [x] ~~Implement GREANCNV~~  
      - [x] ~~Created a column init~~  
      - [x] ~~Need to create column mapping from infoscan~~   
      - [x] ~~computation~~  
      - [x] ~~Save it in the respective folder~~   
    - [ ] Test  
    - [ ] Implement Test Harness   
    - [ ] Do demo to Genpact   
    - [ ] Backup  
  - [ ] **CLSTDICA**  
    - [x] ~~Analyze it well and do implementation md~~  
    - [ ] Create a Master Flow which will have dictionary job has Snippet  
    - [ ] Implement  
    - [x] ~~Analyze PL~~  
    - [ ] After that implement MDWK / MDYAD in a script level  
      - [x] ~~MDWK~~  
      - [ ] MDYAD  
    - [ ] Integrate all into single flow  
    - [ ] Test  
  - [ ] **CLSTMOVA**  
    - [ ] Analyze PL  
- [ ] ***new item and dictupd***   
- [ ] Update DB

- [ ] **Create a df where the discarded records are left and given a reason for the discard**   
- [ ] **Need to implement part before READNEXT  invalid generation**  
- [x] ~~Write about issues in the EUDL Dictionary Job note~~  
- [x] ~~Configure paths, DB Tables, Db names~~    
  - [x] ~~dbname, tablename  parameterze~~  
  - [x] ~~STORMKT  currently ftp, but once table has been provided,   dbname and tablename~~  
- [x] ~~pricereject~~  
- [x] ~~alter table for UK ones , remove aattribut in mainukflow (as there is only one flow)~~  
- [x] ~~Maintain Unit Tests Docs~~  
- [ ] .destroy() broadcast variables used in dict flow  
- [ ] Clean up Script   
  - [ ] Backup File  
  - [ ] Delete   
- [x] ~~Create a Master .sql file for handling tables for other countries~~  
- [x] ~~Verify the columns from the db and the existing identifiers in the code~~



Dec 10, 2025  Dec 14, 2025

- [ ] Learn file manipulation with python and bash  
- [x] ~~Create a FrameWork for handling the python procs~~  
- [x] ~~Backup each ipynb in all dict flow~~   
- [x] ~~Backup dictionary and run itusing update  1~~   
- [ ] **NEWPROC:**  
  - [ ] Need JCL for Audit Programs  
  - [ ] Input Files for the above  
  - [ ] **CPYFKPYT**   
    - [ ] Analyze Basic I/O Processing   
    - [ ] Analyze the Python Program  
    - [ ] Analyze How Parsing Works  
  - [ ] **FRNBATCH**  
  - [x] ~~**EANAUDA**~~  
    - [x] ~~Analyze it and Implement the pl~~  
  - [ ] **EAUDFRMA**  
    - [ ] Analyze PL  
    - [ ] Implement  
  - [ ] **CLSTDICA**  
    - [ ] Create a Master Flow which will have dictionary job has Snippet  
    - [ ] Implement  
    - [ ] Analyze PL  
  - [ ] **CLSTMOVA**  
    - [ ] Analyze PL  
- [x] ~~***CREATE BACKUPS AND ORGANIZE correctly***~~  
- [ ] ***new item and dictupd***  
- [ ] Update DB  
- [x] ~~Learn basic networking command~~  
- [ ] ***WKBKCM2**  EXCEPT UK *   
  - [ ] *Try it with cursor, explore*  
- [ ] 

Dec 1, 2025  

- [ ] Learn file manipulation with python and bash   
- [ ] Learn basic networking command  
- [ ] Update DB  
- [ ] *Fix Descr in current*  
- [ ] ***CREATE BACKUPS AND ORGANIZE correctly***  
- [ ] ***new item***  
- [ ] ***WKBKCM2**  EXCEPT UK *   
  - [ ] *Try it with cursor, explore*  
- [ ] ***NEWPROC:***  
  - [x] ~~Complete CENMERGE~~   
    - [x] ~~analyze , edit in New proc  algo, dependencies, datasets~~  
    - [x] ~~pull all the files needed~~  
    - [x] ~~Implement it in IS~~  
    - [x] ~~triggerDictionary~~    
    - [x] ~~Implement storing of Files~~  
  - [ ] Complete CPYFKPYT  
    - [ ] analyze and edit in New Proc  
    - [ ] Pull all files needed  
    - [ ] Implement it in python  
  - [ ] EUNAUDA  
  - [ ] EUAUFRMA    
    - [ ] analyze and edit in New Proc  
    - [ ] Pull all files needed  
  - [ ] FRNBATCH    
    - [ ] Analyze UGO.SCENDICT  
    - [ ] Analyze UGO.SCENMOVE  
    - [ ] Create python code for calling tape

25/11/2025  27/11/2025

- [ ] ***new item***  
- [ ] ***WKBKCM2**  EXCEPT UK *   
  - [ ] *Try it with cursor, explore*  
- [x] ~~*Develop a Script to copy from existing table to current table  .sql*~~   
- [ ] ***NEWPROC:***  
  - [ ] *Analyze CENMERGE*  
  - [ ] *get QCPROC from Sample Team*  
  - [ ] *Analyze and implement CPYFKPYT*  
  - [x] ~~*ask pl programs for audit and files*~~  
  - [x] ~~*Change the TRANS2U   to show it to*~~   
  - [x] ~~*Add QC check to TRANS2U and CPYFK, like it should prompt for override*~~   
  - [x] ~~*Analyze*~~   
- [x] ~~*Look into HTTPAuth and Token  how is it different how the server will accept two ways of auth,*~~   
- [ ] ***CREATE BACKUPS AND ORGANIZE correctly***  
- [x] ~~what is the problem in alphadescr  Respond to Test case France~~ 

21/11/2025

- [ ] ***Analyze New Item File  ***   
- [ ] ***WKBKCM2**  EXCEPT UK *   
  - [ ] Try it with cursor, explore  
- [ ] Develop a Script to copy from existing table to current table  .sql   
- [ ] Discuss about Flat structure  
- [ ] MCP, server  
- [ ] Dictionary  
- [ ] **CREATE BACKUPS AND ORGANIZE correctly**  
- [x] ~~**add if following parameters are not found , fail the flow**~~   
- [ ] **new item ftp**  
- [ ] **NEW PROC :**  
  - [ ] Bring CENMERGE  Nov 21, 2025 call  
  - [x] ~~watch kt videos and populate  CENMERGE, FRNBATCH, CPYKFPT~~  
  - [ ] cli way  
  - [x] ~~Literal Conversion of TRANS2U  paramiko~~  
  - [x] ~~list out dependencies,~~   
  - [x] ~~How main flows can be triggered from this new proc~~  
  - [x] ~~list out different files~~ 

10/11/2025  20/11/2025

- [ ] ***Analyze New Item File  ***   
- [x] ~~***Analyze France and DICTUPD***~~  
- [ ] ***WKBKCM2**  EXCEPT UK *   
  - [ ] Try it with cursor, explore  
- [ ] Develop a Script to copy from existing table to current table  .sql   
- [x] ~~Develop a py script that can check files listed in a text file present in the given file or not~~   
- [x] ~~Store Output Files, **Need to have input files for Dictionary Causal~~**   
- [ ] Discuss about Flat structure  
- [ ] MCP, server  
- [ ] Dictionary  
- [ ] **CREATE BACKUPS AND ORGANIZE correctly**  
- [x] ~~**remove isCausal in dictionary , call causal directly and pass isCausalProcess**~~  
- [x] ~~**add isCausal Flow control**~~   
- [x] ~~**add causal job triggering and test it**~~  
- [x] ~~**test move job triggering and test it**~~   
- [x] ~~**send parameters to tape job**~~  
- [x] ~~Implement Storing files~~  
  - [x] ~~change isCausal False , Copy triggerCausal , Copy from ALLDICTIONARY~~  
  - [ ] implement triggerMove Directly   
  - [ ] put branch here save Output in FTP  
  - [ ] do the same for causal Dictionary  
- [x] ~~Causal Dictionary  calling via get request~~

3/11/2025  8/11/2025

- [x] ~~**Test Causal Dictionary  i**~~  
- [x] ~~**Add API Input in Causal Flow**~~   
- [x] ~~**Refactor and Fix Apply Causal to Sales Data ISEUDL**~~   
- [x] ~~Add WKBPCAUL  WKBPCAUW~~   
- [x] ~~**Refactor Existing ALL Dictionary Job  i**~~  
  - [x] ~~Export the isx, add parameter and if it is yes trigger the flow~~   
  - [x] ~~Remove Last step ,~~  
  - [x] ~~inside Causal Add Move triggering~~   
  - [ ] 
- [x] ~~**Prepare a Country Level Difference Document**~~   
- [ ] ***Analyze New Item File  ***   
- [ ] ***Analyze France ~~MULT~~ and DICTUPD***  
- [ ] ***WKBKCM2**  EXCEPT UK *   
- [x] ~~See when was the dictionary lastly updated~~  
  - [ ] (optional) how we can sync up two tables  
- [ ] Bash script to copy files and periodically and then   
- [ ] *EXEC SERV  Meaning*

21/10/2025  31/10/2025

- [ ] Analyze **New Item File**   
- [ ] Analyze France MULT and DICTUPD  
- [x] ~~ICAUDIT FILE  push~~  
- [x] ~~Existing PROCs~~  
- [ ] **UAT**  
  - [x] ~~Include **apibaseurl** in parameter, store db **username**, **password**, dictdb **username** , **password , DEV  [Janaranjan E~~](mailto:janaranjan.e@blackstraw.ai)**  
  - [ ] Single Dataframe approach  Stat  [SR Vasanthan](mailto:sr.vasanthan@blackstraw.ai)  
  - [ ] 
  - [x] ~~Remove publish Content list of username for prod  [Janaranjan E](mailto:janaranjan.e@blackstraw.ai)~~	  
- [x] ~~Integrate Chain Level Imputation  part~~  
- [x] ~~Run Germany~~  
- [x] ~~List out missing procs Oct 22, 2025 3:00 PM~~   
- [ ] **WKBKCM2**  EXCEPT UK  
- [ ] EXEC SERV  Meaning  
- [x] ~~Holland E2E~~

9/10/2025

- [ ] New PROC  
  - [ ] Infoscan vs EUROscan  
  - [ ] Sample vs Census vs Causal  
  - [ ] Baseline file   
  - [ ] ICAAUDIT File definition  
  - [ ] FEATURE FILE  
- [x] ~~New Item File Creation~~  
  - [x] ~~Convert to CSV~~  
  - [ ] then CSV To SCRIPT FTP  
- [ ] Weekdata  
  - [ ] do a branch then do it  
  - [ ] Convert to CSV  
  - [ ] then CSV to Script FTP  
- [ ] Complete Stat  
- [ ] Do Chain Level Imputation to make the process skip whole dictionary job  
- [x] ~~Set tape parameter for dictoutput, CHAINLEVELIMPUTATION~~  
- [ ] *Check why update value is showing a different one than for a*   
- [ ] *Unit Test params*  
  - [ ] *Unique UPC count movein*  
  - [ ] *New Item Flag to be 1 count*  
  - [ ] ***New Item Creation***  
  - [ ] *Rephrase the Flow Stat*  
  - [ ] 
- [ ] 

3/10/2025

- [ ] New Item File Creation  
  - [ ] Convert to CSV  
  - [ ] then CSV To SCRIPT FTP  
- [ ] Weekdata  
  - [ ] do a branch then do it  
  - [ ] Convert to CSV  
  - [ ] then CSV to Script FTP  
- [ ] Complete Stat  
- [ ] Set tape parameter for dictoutput, CHAINLEVELIMPUTATION  
- [ ] *Check why update value is showing a different one than for a*   
- [ ] *Unit Test params*  
  - [ ] *Unique UPC count movein*  
  - [ ] *New Item Flag to be 1 count*  
  - [ ] ***New Item Creation***  
  - [ ] *Rephrase the Flow Stat*  
  - [ ] 



2/10/2025

- [x] ~~*Update Working*~~  
  - [x] ~~*change Pricereject , schema*~~  
  - [x] ~~*add raise Error before update query check the dicti record and wlm , wad and in wadtable*~~  
- [ ] *Check why update value is showing a different one than for a*   
- [ ] *Tests For Italy⌛*  
  - [ ] *Change the db for UPDATE late week query*   
  - [x]  ~~***Unit Level Test Pending*~~**    
  - [ ]  ***Update Logic***   
  - [ ]  *Back week run*  
- [ ] *Tests For Holland ⌛*  
  - [x]  ~~***Unit Level Test Pending*~~**   
  - [x]  ~~***Update Logic*~~**   
  - [ ]  *Back week run*  
- [ ] *Tests For UK ⌛*  
  - [ ] *Change the db for UPDATE late week query or run all query*  
  - [ ] *Alter price  pricereject in the table*  
  - [ ]  ***Unit Level Test Pending***   
  - [ ]  ***Update Logic***   
  - [ ]  *Back week run*  
- [ ] *Count New Item UPC*   
- [ ] *Count NewItemFlag  New Item Creation condition checked  and see counts are happening*   
- [ ] *Total Records created count should match with total stores count  Create a variable called uniqueStores in FIxer*   
  - [ ] *Spark SQL*  
- [ ] *Handle pricerejct columns  pricereject, **Rajesh***  
- [ ] *Refactor Codebase*

29/09/2025

- [x] ~~*See the Recordings*~~  
- [x] ~~*Ready the db for UK  indexing on wad*~~   
- [x] ~~Take the latest wad or wlm when updating with table in setup query~~  
- [ ] price Reject  change it   
- [x] ~~Create Table for UK ~~   
- [ ] Change the update logic to include the latest wlm , wad in the ukmfdictionary  
- [x] ~~Change the api params to mariam job  triggerAPI~~  
- [ ] *Tests For Italy⌛*  
  - [x]  ~~***Unit Level Test Pending*~~**    
  - [ ]  ***Update Logic***   
  - [ ]  *Back week run*  
- [ ] *Test for UK*  
  - [ ] *Unit Level Test*  
  - [ ] *Update Logic*  
  - [ ] *Backweek run*  
- [ ] *Tests For Holland ⌛*  
  - [ ]  ***Unit Level Test Pending***   
  - [ ]  ***Update Logic***   
  - [ ]  *Back week run*  
- [ ] *Count New Item UPC*   
- [ ] *Count NewItemFlag  New Item Creation condition checked  and see counts are happening*   
- [ ] *Total Records created count should match with total stores count  Create a variable called uniqueStores in FIxer*   
  - [ ] *Spark SQL*  
- [ ] *Handle pricerejct columns  pricereject, **Rajesh***  
- [ ] *Refactor Codebase*

24/09/2025  26/09/2025

- [x] ~~Do all the counts stat~~  
- [ ] See the Recordings  
- [ ] *Tests For Italy⌛*  
  - [ ]  ***Unit Level Test Pending***    
  - [ ]  ***Update Logic***   
  - [ ]  *Back week run*  
- [ ] *Tests For Holland ⌛*  
  - [ ]  ***Unit Level Test Pending***   
  - [ ]  ***Update Logic***   
  - [ ]  *Back week run*  
- [ ] *Develop Unit Test Data*   
- [ ] Test for UK  
  - [ ] Unit Level Test  
  - [ ] Update Logic  
  - [ ] Backweek run  
- [x] ~~*Extract what fields in iritem , Dictionary is changed in Each **Units  ??[Janaranjan E](mailto:janaranjan.e@blackstraw.ai)*~~**   
- [x] ~~*Count total New Items  and explain it with some reason like status  old gen , no dictionary record available  New Item Flag  1*~~  
- [ ] *Count New Item UPC*   
- [ ] *Count NewItemFlag  New Item Creation condition checked  and see counts are happening*   
- [ ] *Total Records created count should match with total stores count  Create a variable called uniqueStores in FIxer*   
  - [ ] *Spark SQL*  
- [ ] *Handle pricerejct columns  pricereject, **Rajesh***  
- [ ] Refactor Codebase

19/09/2025  23/09/2025

- [x] ~~Put files in weekdata and newitem   [SR Vasanthan](mailto:sr.vasanthan@blackstraw.ai)   ask regarding dharshan~~   
- [x] ~~Create API Input for the Dict General FLow~~  
- [ ] See the Recordings  
- [x] ~~**IMPLEMENT New Item Flag for all the items in the iritem set, [SR Vasanthan**](mailto:sr.vasanthan@blackstraw.ai)~~  
  - [ ] Once its done   
- [ ] *Tests For Holland ⌛*  
  - [ ]  *Unit Level Test Pending*   
  - [ ]  *Update Logic*  
  - [ ]  *Back week run*  
- [ ] *Develop Unit Test Data*   
  - [x] ~~*Split the Job into each **Units*~~**  
  - [x] ~~*With copilot just see how will the process differ when we change the week or any other parameter*~~  
  - [x] ~~*Extract what fields in iritem , Dictionary is changed in Each **Units  ??[Janaranjan E](mailto:janaranjan.e@blackstraw.ai)*~~**   
  - [x] ~~*Check DB is connected or not and it is respective to the correct country   change dictionary schema  countryid for different countries  Linker*~~  
  - [x] ~~*if a dictionary read happens, denote it with some special flag*~~    
  - [ ] *Count total New Items  and explain it with some reason like status  old gen , no dictionary record available  New Item Flag  1*  
  - [ ] *Count New Item UPC*    
  - [x] ~~*Count dctwrtx called*~~  
  - [x] ~~*Dictupdx query  table [Janaranjan E*](mailto:janaranjan.e@blackstraw.ai)~~  
  - [x] ~~*Count olddictcount  **create a function to retrieve the count from the database    Linker*~~**  
  - [x] ~~*Count Dictionary Updates count  dctupdx called*~~     
  - [ ] *Count NewItemFlag  New Item Creation condition checked  and see counts are happening*   
  - [ ] *Total Records created count should match with total stores count  Create a variable called uniqueStores in FIxer*   
  - [ ] ~~*Create a golden dataset which has :halt*~~  
- [x] ~~*Backup*~~  
- [x] ~~*SQL  Index  ⌛*~~  
  - [ ] *Spark SQL*  
- [ ] *Handle pricerejct columns  pricereject, **Rajesh***

18/09/2025

- [ ] Tests For Holland ⌛  
  - [ ]  Unit Level Test Pending   
  - [ ]  Update Logic  
  - [ ]  Back week run  
- [ ] *Develop Unit Test Data*   
  - [x] ~~*Split the Job into each **Units*~~**  
  - [ ] *With copilot just see how will the process differ when we change the week or any other parameter*  
  - [ ] *Extract what fields in iritem , Dictionary is changed in Each **Units***  
  - [ ] *if a dictionary read happens, denote it with some special flag*   
  - [ ] *Create a golden dataset which has*   
- [ ] *Backup*  
- [ ] *SQL  Index  ⌛*  
  - [ ] *Spark SQL*  
- [ ] *Handle pricerejct columns  pricereject,*  
- [x] ~~NewItemFlag  1  [Janaranjan E](mailto:janaranjan.e@blackstraw.ai)~~  
- [ ] 

15/09/2025  17/09/2025

- [x] ~~Setup DB for France [Janaranjan E](mailto:janaranjan.e@blackstraw.ai)~~	  
- [x] ~~Setup DB For Germany [SR Vasanthan](mailto:sr.vasanthan@blackstraw.ai)~~  
- [ ] Tests For Holland ⌛  
  - [x] ~~Run Completion~~  
  - [x] ~~Harness Check  (TGENERATION few, FEATURECODES)~~  
- [ ] Develop Unit Test Data   
  - [ ] Split the Job into each **Units**  
  - [ ] With copilot just see how will the process differ when we change the week or any other parameter  
  - [ ] Extract what fields in iritem , Dictionary is changed in Each **Units**  
  - [ ] *if a dictionary read happens, denote it with some special flag*   
  - [ ] Create a golden dataset which has   
- [ ] *Handle pricerejct columns  pricereject,*  
- [ ] *Create a FTP to DF Script  dict cols, stdcols*  
- [ ] Backup  
- [ ] SQL  Index  ⌛  
  - [ ] Spark SQL

11/09/2025  12/09/2025

- [ ] *Handle pricerejct columns  pricereject, [SR Vasanthan](mailto:sr.vasanthan@blackstraw.ai)*  
- [ ] *Get the Unit Test  [SR Vasanthan](mailto:sr.vasanthan@blackstraw.ai)*   
  - [ ] *FLow Run*  
  - [ ] *COunt Mismatch*  
  - [ ] *Dict Read*    
  - [ ] *Flag setting for each functions*   
  - [ ] *Verify Dict before Updating*   
- [ ] *SQL  basics*   
- [x] ~~STORMKT  currently ftp, but once table has been provided,   dbname and tablename~~  
- [x] ~~*Create a Script To Extract STORMKT as Table [SR Vasanthan*](mailto:sr.vasanthan@blackstraw.ai)~~   
- [ ] Run for Holland [SR Vasanthan](mailto:sr.vasanthan@blackstraw.ai)  
- [ ] Test For Holland [SR Vasanthan](mailto:sr.vasanthan@blackstraw.ai)  
- [ ] Backup  
- [x] ~~Debug upto main dictionary update~~    
  - [ ] Dynamic Price Override  [Janaranjan E](mailto:janaranjan.e@blackstraw.ai)  
  - [ ] Process Hicones  [Janaranjan E](mailto:janaranjan.e@blackstraw.ai)  
  - [x] ~~Overall Processing for set of items  [Janaranjan E](mailto:janaranjan.e@blackstraw.ai)~~



08/09/2025  10/09/2025

- [ ] Makeup table  Holland [Janaranjan E](mailto:janaranjan.e@blackstraw.ai)  
- [x] ~~Debug the gen  1 values  (due to calling of initialize dict structure in read part)~~  
- [x] ~~Debug upto main dictionary update [Janaranjan E](mailto:janaranjan.e@blackstraw.ai)  imu~~   
- [ ] Backup

- [x] ~~Country wise database changes  added five params,~~   
- [ ] Handle pricerejct columns  pricereject, [SR Vasanthan](mailto:sr.vasanthan@blackstraw.ai)  
- [ ] SQL  basics   
- [ ] Get the Unit Test  [SR Vasanthan](mailto:sr.vasanthan@blackstraw.ai)   
  - [ ] FLow Run  
  - [ ] COunt Mismatch  
  - [ ] Dict Read    
  - [ ] Flag setting for each functions   
  - [ ] Verify Dict before Updating    
- [x] ~~Create a Script To Extract STORMKT as Table [SR Vasanthan](mailto:sr.vasanthan@blackstraw.ai)~~   
- [ ] 

05/09/2025

- [ ] Create Indices and alter types for the Holland DB  
- [ ] Handle pricerejct columns  pricereject,   
- [ ] Resolve TGENERATION and solve MFBCAT AND KEYCAT Problems   
  - [x] ~~add wad, wlm, and gen from the dictionary and add it to~~  
  - [ ] Enquire Readings  
- [ ] Debug upto main dictionary update  
- [ ] Create main dict flow in single script using spark   
  - [x] ~~copy flow~~   
  - [ ] get the TUpc values in single list declare

03/09/2025

- [x] ~~Add integer column in mfdictionary~~  
- [x] ~~Change the logic in query when doing so , so it should fetch only one record and see for which market field or weeks added we are setting are we setting for all market bits or only one record,~~   
  - [ ] try to do a left join only for one record and add index for market also  
- [ ] Try to create table out of wad and wlm and market in incorporate in   
  - [ ] Try doing the same for Spain or France with singular market number  
- [ ] 

02/09/2025

- [ ] Fix TGENERATION  read not happening   
- [ ] Fix MFBCAT, KEYCAT  dictionary read bug

—---------------------------------------------------------------------------------------------------------------------------

- [x] ~~Complete it Before Thursday  Give a Demo~~  
- [x] ~~Refactor Names in Scripts~~  
- [ ] Change types in Main Dict Script  
- [x] ~~**While Orchestration Make sure to add a Pre Script at front after API to convert the column name to program context columns**~~   
- [ ] **Create a df where the discarded records are left and given a reason for the discard**   
- [x] ~~**add IRISTORE for joining store number**~~   
- [x] ~~Make the Flow to be General~~  
- [x] ~~price logic~~  
- [x] ~~process-hicones~~  
- [x] ~~MainScript~~  
- [ ] **Need to implement part before READNEXT  invalid generation**  
- [x] ~~**Add STORINFO at last , like getting its value from the MainDictionary Read and after in consolidated we** get its other fields outcount and dollars and join it~~   
- [ ] MileStone Preservation  
- [ ] Configure paths, DB Tables, Db names  
  - [ ] dbname, tablename  parameterze  
  - [ ] STORMKT  currently ftp, but once table has been provided,   dbname and tablename  
- [ ] pricereject  
- [ ] alter table for UK ones , remove aattribut in mainukflow  
- [ ] Maintain Unit Tests Docs

1/09/2025

- [ ] Take Schema from the Dictionary Highlight the important ones  
- [x] ~~Perform Schema Checks~~   
  - [x] ~~Italy~~  
  - [x] ~~Spain~~  
  - [x] ~~NL~~  
  - [x] ~~HL~~  
  - [x] ~~DE~~  
- [x] ~~Try inserting to the tables~~  
- [ ] Fix ALPHA DESCR  
  - [ ] do a harness report on raw and weekdata directly see , incorrect ness,   
- [ ] Fix TGENERATION    
  - [x] ~~check from db and do the checks one with incorrect ones  [Janaranjan E](mailto:janaranjan.e@blackstraw.ai)~~  
  - [x] ~~See where in the code we are reading the gen and what value is coming and see where it is being manipulated,~~   
    - [ ] code by glance  
    - [ ] during execution  
  - [ ] 
- [ ] Fix MFBCAT, KEYCAT  
  - [ ] check group by values from mfbcat  
  - [ ] extract all data from italy and then perform join for the weekdata df  [Janaranjan E](mailto:janaranjan.e@blackstraw.ai)  
  - [ ] 
- [ ] Backup db dump

29/08/2025

- [x] ~~Perform Explain Operation , analyze~~  
- [ ] How repartition works and mapPartitions and functions and how yield and spark. createDataframe and collect works   
- [x] ~~Try changing the types , – UNIFY the types adn remove ::text in queries~~  
- [x] ~~Attribute table joins  find cost~~  
- [ ] Remove attribute table and see if it works

28/08/2025

- [ ] Fix Main Dict Read  
  - [x] ~~Check table indexed or not~~   
  - [ ] Remove Print   
  - [ ] Run using collec  
    - [ ] take 10 records using loop , call dictread and just check performance for   
      - [ ] Italy   
      - [ ] UK  upd ,   
      - [ ] UK  general flow  33 secs  
    - [ ] 

25/08/2025

- [x] ~~Create a backup it dictionary table~~  
  - [x] ~~then copy values from wlm, waad~~  
- [x] ~~change to different database, dictit~~   
- [x] ~~Retrieve file for 2389 , 8H~~  
- [ ] Test for 2389 8H  
- [ ] Create a Columns required for each Major Components, eg: StoreNumber ,   
- [ ] *Linux directories, quizzes*

22/08/2025

- [ ] Check the current db values in shell,  
  - [ ] count  
  - [ ] take not of the fields which we will be updating in the dictionary   
  - [ ] take 1 item from jso h9, and put debug statements   
  - [ ] and check with debug statements actual table 

21/08/2025

- [ ] Dictionary Updation   check if it correctly updating in   
- [ ] UPDATE = 1, different table  
  - [x] ~~verify the other table~~  
- [ ] *Passport Strategy, Perform Add to Cart functionality ,*   
- [ ] *complete csbase01* 

18/08/2025

- [ ] Copy upd flow to UPDATION , make changes  
  - [x] ~~backup UPDATION~~  
  - [x] ~~backup upd~~  
  - [x] ~~analyze and compare both flows component by component~~  
  - [x] ~~copy Main Dict flow from UPDATION to upd~~  
- [ ] Do Testing on UPDATION , Compare with existing upd or updation make sure it is not failing 

11/08/2025

- [ ] ~~Change the FTP path to be dynamic for EXTRMKT,~~    
- [x] ~~Need new dictionary or the ukmfdictionary should have wlm ,~~   
- [ ] Compare both upd, DICT UPDATION flow . test rigorously for  
  - [ ] SDC 2394  
    - [ ] tst  
      - [x] ~~df generated~~  
      - [x] ~~tested harness~~  
    - [ ] bkv1  
      - [x] ~~df generated~~  
      - [x] ~~tested harness~~  
  - [ ] SDC 2380  
    - [ ] tst  
      - [ ] df generated  
      - [ ] tested harness  
    - [ ] bkv1  
      - [ ] df generated  
      - [ ] tested harness  
  - [ ] JSO 2395  
    - [x] ~~tst~~  
      - [x] ~~df generated~~  
      - [x] ~~tested harness~~  
    - [x] ~~bkv1~~  
      - [x] ~~df generated~~  
      - [x] ~~tested harness~~  
  - [ ] tst and bkv1  
- [x] ~~Need to discuss with movejob for stormkt~~  
- [x] ~~verify store master~~   
- [x] ~~Export the flow,~~

07/08/2025

- [ ] Learn remote command, sudo  
- [ ] 
- [x] ~~Try to do sorting with store numbers inside groupeed~~  
- [ ] *Compare Both test and upd flows and then test it for SPD and JSO chain*   
  - [x] ~~***Try running it in design mode***~~  
  - [x] ~~*FIrst compare code*~~  
  - [x] ~~*Run for JSO*~~  
  - [x] ~~*Then run it for JSO update  0*~~   
  - [x] ~~*Test Harness same percentage*~~  
- [ ] *Debug for Dict that correct it gets updated in various step or not , track the flow [Janaranjan E](mailto:janaranjan.e@blackstraw.ai)*  
  - [ ] *during read,*   
- [ ] *Ensure before and after values of updated Dict Values*  
- [x] ~~*Try to a diagrammatic representation of how the partition of upc is working*~~   
- [x] ~~*Back Week Processing  Analyze it  and Test it*~~  
- [x] ~~*Analyze the partition and DPO and process hicones once more*~~  



06/08/2025

- [ ] Compare Both test and upd flows and then test it for SPD and JSO chain   
  - [ ] FIrst compare code  
  - [ ] Run for JSO  
  - [ ] Then run it for JSO update  0   
  - [ ] Test Harness same percentage  
- [ ] Debug for Dict that correct it gets updated in various step or not , track the flow [Janaranjan E](mailto:janaranjan.e@blackstraw.ai)  
  - [ ] during read,   
- [ ] Ensure before and after values of updated Dict Values  
- [x] ~~Try to a diagrammatic representation of how the partition of upc is working~~   
- [ ] Back Week Processing  Analyze it  and Test it  
- [ ] Analyze the partition and DPO and process hicones once more    

04/08/2025

- [ ] add a script before at start fail the flow if the dataframe has no , status, footprint bits   
- [ ] Ensure New Item is created  
- [x] ~~New Item Flag  KEYCAT, MFBCAT~~

30/07/2025

- [ ] Try to a diagrammatic representation of how the partition of upc is working   
- [ ] Try to give a status message in context,   
- [ ] add a script before at start fail the flow if the dataframe has no , status, footprint bits   
- [x] ~~Backup the flow scripts once after demo 1~~   
- [x] ~~Fix the STORTYP issue~~  
- [ ] Back Week Processing  Analyze it  and Test it  
- [x] ~~Try Running using batch and ensure no error is happening~~   
- [x] ~~Trigger with UPDATE  0~~  
- [ ] Ensure New Item is created  
- [x] ~~Change to Old db~~    
- [x] ~~Try running manual DIct updation~~  
- [ ] Create a another script which uses collect()   
- [x] ~~Write a Comparison Report~~   
  - [x] ~~Get Script from Naveen~~ 

29/07/2025

- [ ] Add jana to the shared published  
- [x] ~~Test Batch Run UKFlow  issue fixed width parser failed  need to implement script~~  
- [x] ~~Fix STORMKT, Remove Junction~~  
- [x] ~~Communicate with Move job for output~~  
- [x] ~~hANDLE FIELD MISMATCH ERROR~~  
- [x] ~~Try triggering mariam’s flow,~~   
- [x] ~~Try implementing snippet ,and how we can do with file mask~~

28/07/2025

- [x] ~~Fix the consolidated~~   
- [x] ~~Add tagging component , CHAINID~~  
- [x] ~~Test Batch Run UKFlow~~  
- [x] ~~Test for latest week~~  
- [ ] **While Orchestration Make sure to add a Pre Script at front after API to convert the column name to program context columns**   
- [x] ~~Trigger Move~~  
- [x] ~~Demo~~   
  - [x] ~~Create a Presentation~~

23/07/2025

- [x] ~~Flow Properties  Dictionary Job~~  
- [x] ~~After API call, Tag name  cluster,~~ 

22/07/2025

- [ ] **FIX FOR UK**   
  - [ ] **Run For different current week  currently doing for 2387**  
  - [ ] Look For ISSUES  invalid   
  - [ ] **Implement STORINFO values to be preserved**   
  - [ ] **Use STORINFO values after program termination and then use it for adding Total Store records**  
    - [x] ~~Fixt the existing issue  storinfostore  issue solved~~  
    - [ ] Change Main DIctionary Read    
    - [ ] Change Consolidated  
    - [ ] Implement the storinfofootprint changes   
    - [ ] Add Total Store recored  
- [ ] See how mapParition is working  
- [ ] Re-verify the Script  
- [ ] 
- [ ] A datalake.  
- [ ] **test for all the items in dictionary   that for all test cases it should handle like if**   
  - [ ] string , int when item in the dictionary is of different type  
- [ ] find a way to implement logging like when the item is invalid or just discarded , should increase the Global Counter  
- [ ] DataFrames  
- [ ] How Join Works in SQL, spark , anti join  
- [ ] spark streaming  
- [ ] Accumulators  
- [ ] 

21/07/2025

- [ ] **FIX FOR UK**   
  - [ ] **Run For different current week  currently doing for 2387**  
  - [ ] Look For ISSUES  invalid   
  - [ ] **Implement STORINFO values to be preserved**   
  - [ ] **Use STORINFO values after program termination and then use it for adding Total Store records**  
- [ ] Re-verify the Script  
- [ ] 
- [ ] A datalake.  
- [ ] **test for all the items in dictionary   that for all test cases it should handle like if**   
  - [ ] string , int when item in the dictionary is of different type  
- [ ] find a way to implement logging like when the item is invalid or just discarded , should increase the Global Counter  
- [ ] DataFrames  
- [ ] How Join Works in SQL, spark , anti join  
- [ ] spark streaming  
- [ ] Accumulators

18/07/2025

- [ ] **FIX FOR UK**   
  - [ ] **Run For different current week  currently doing for 2387**  
  - [ ] Look For ISSUES  invalid   
  - [ ] **Implement STORINFO values to be preserved**   
  - [ ] **Use STORINFO values after program termination and then use it for adding Total Store records**  
- [ ] Re-verify the Script  
- [ ] A datalake.  
- [ ] **test for all the items in dictionary   that for all test cases it should handle like if**   
  - [ ] string , int when item in the dictionary is of different type  
- [ ] find a way to implement logging like when the item is invalid or just discarded , should increase the Global Counter  
- [ ] DataFrames  
- [ ] How Join Works in SQL, spark , anti join  
- [ ] spark streaming  
- [ ] Accumulators  
- [ ] stdout, stdin   
  - [ ] [https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.htmlpyspark.RDD](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.html#pyspark.RDD)  
  - [ ] [https://spark.apache.org/examples.html](https://spark.apache.org/examples.html)

17/07/2025

- [x] ~~Try to Load file using Script FTP~~  
- [x] ~~after that, check for that store~~   
- [x] ~~and if now then check how many records does that have that store number, we can remove it and note somewhere~~  
- [ ] After that try to complete the remaining single script logic

16/07/2025

- [ ] **FIX FOR UK**   
  - [ ] **Run For different current week  currently doing for 2387**  
  - [ ] Look For ISSUES  invalid   
- [ ] Re-verify the Script  
- [ ] A datalake.  
- [ ] **test for all the items in dictionary   that for all test cases it should handle like if**   
  - [ ] string , int when item in the dictionary is of different type  
- [ ] find a way to implement logging like when the item is invalid or just discarded , should increase the Global Counter  
- [ ] DataFrames  
- [ ] How Join Works in SQL, spark , anti join  
- [ ] spark streaming  
- [ ] Accumulators  
- [ ] stdout, stdin   
  - [ ] [https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.htmlpyspark.RDD](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.html#pyspark.RDD)  
  - [ ] [https://spark.apache.org/examples.html](https://spark.apache.org/examples.html)  
- [ ] 

15/07/2025

- [ ] **FIX FOR UK**   
  - [ ] **Run For different current week  currently doing for 2387**  
  - [x] ~~Look For ISSUES  invalid storenumber (we got latest stormkt)~~  
- [ ] Re-verify the Script  
- [ ] A datalake.  
- [ ] **test for all the items in dictionary   that for all test cases it should handle like if**   
  - [ ] string , int when item in the dictionary is of different type  
- [ ] find a way to implement logging like when the item is invalid or just discarded , should increase the Global Counter  
- [ ] DataFrames  
- [ ] How Join Works in SQL, spark , anti join  
- [ ] spark streaming  
- [ ] Accumulators  
- [ ] stdout, stdin   
  - [ ] [https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.htmlpyspark.RDD](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.html#pyspark.RDD)  
  - [ ] [https://spark.apache.org/examples.html](https://spark.apache.org/examples.html)

11/07/2025

- [ ] **FIX FOR UK**   
  - [ ] **Run For different current week**   
  - [ ] Look For ISSUES  
- [ ] Re-verify the Script  
- [ ] A datalake.  
- [ ] **test for all the items in dictionary   that for all test cases it should handle like if**   
  - [ ] string , int when item in the dictionary is of different type  
- [ ] find a way to implement logging like when the item is invalid or just discarded , should increase the Global Counter  
- [ ] DataFrames  
- [ ] How Join Works in SQL, spark , anti join  
- [ ] spark streaming  
- [ ] Accumulators  
- [ ] stdout, stdin   
  - [ ] [https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.htmlpyspark.RDD](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.html#pyspark.RDD)  
  - [ ] [https://spark.apache.org/examples.html](https://spark.apache.org/examples.html)  
  - [ ] the [configuration](https://spark.apache.org/docs/latest/configuration.html) and [tuning](https://spark.apache.org/docs/latest/tuning.html) g



9/07/2025

- [ ] **FIX FOR UK**   
  - [ ] **Run For different current week**   
  - [ ] Look For ISSUES  
- [ ] Re-verify the Script  
- [x] ~~If you understand SparkContext, SparkSession, RDD and Lazy Evaluation, you're good.~~  
- [ ] A datalake.  
- [ ] **test for all the items in dictionary   that for all test cases it should handle like if**   
  - [ ] string , int when item in the dictionary is of different type  
- [ ] find a way to implement logging like when the item is invalid or just discarded , should increase the Global Counter  
- [x] ~~Driver & Executors~~  
- [ ] RDD and DataFrames  
- [x] ~~Lazy Evaluation~~  
- [ ] How Join Works in SQL, spark , anti join  
- [ ] spark streaming

8/07/2025

- [ ] **FIX FOR UK**   
  - [ ] **Run For different current week**   
  - [ ] Look For ISSUES  
- [ ] Re-verify the Script  
- [ ] **test for all the items in dictionary   that for all test cases it should handle like if**   
  - [ ] string , int when item in the dictionary is of different type  
- [ ] find a way to implement logging like when the item is invalid or just discarded , should increase the Global Counter  
- [ ] Find a way to compare two records  
- [ ] Experiment with Window

- [ ] Understand the differences between parallel computing vs distributed computing (when you can use one or another, when not). Understand very well how the MapReduce paradigm works is veeeery important. If you know what is the problem behind working with multiplicand in distributed systems and small files problem, you're very well.  
- [ ] If you understand SparkContext, SparkSession, RDD and Lazy Evaluation, you're good.  
- [ ] A datalake.

7/07/2025

- [x] ~~**SYSTEM REPORT, UKPLU  For the subsequent items also the storinfo value will not be added fix it**~~    
  - [x] ~~Try to test  go for 5validate and check the cell 6~~  
- [ ] **Run For different current week**   
- [ ] Re-verify the Script  
- [ ] test for all the items in dictionary   that for all test cases it should handle like if   
  - [ ] string , int when item in the dictionary is of different type  
- [ ] find a way to implement logging like when the item is invalid or just discarded , should increase the Global Counter  
- [x] ~~Country wise table changes~~  
- [x] ~~**Difference between broadcasting and using class**~~   
- [x] ~~What is Vectorized~~

4/07/2025

- [ ] **SYSTEM REPORT, UKPLU  For the subsequent items also the storinfo value will not be added fix it**    
- [ ] **Run For different current week**   
- [x] ~~**Dictionary Schema changes, fetching and updating from multiple tables**~~   
  - [x] ~~attribute table affected,~~   
  - [x] ~~other not affected may be because of conn.commit()~~  
  - [x] ~~Need to add now() Default for test tables~~  
- [ ] Re-verify the Script  
- [ ] test for all the items in dictionary   
- [x] ~~Simulate run for the updated query and update the dctread func~~  
- [x] ~~Need to update market bit field, wadbit, wlmbit~~  
- [x] ~~Change flow for EXTRMKT ;- flow branch~~  
- [ ] Implement logging  
- [ ] DICT.LASTUPDT        DATE                                 ;  
- [ ] IF DICT.LASTUPDT = 981201 THEN  
- [ ] DICT.LASTUPDT  DICT.LASTUPDT  19000000;  
- [ ] ELSE DICT.LASTUPDT  DICT.LASTUPDT  20000000;  / PRSHS /  
- [ ] 

2/07/2025

- [ ] **SYSTEM REPORT, UKPLU  For the subsequent items also the storinfo value will not be added fix it**    
- [ ] **Run For different current week**   
- [ ] **Dictionary Schema changes, fetching and updating from multiple tables**   
  - [ ] attribute table affected,   
  - [ ] other not affected may be because of conn.commit()  
  - [ ] Need to add now() Default for test tables  
- [ ] Re-verify the Script  
- [ ] test for all the items in dictionary   
- [x] ~~Simulate run for the updated query and update the dctread func~~  
- [ ] Need to update market bit field, wadbit, wlmbit  
- [x] ~~Change flow for EXTRMKT ;- flow branch~~  
- [ ] Implement logging

30/06/2025

- [ ] **SYSTEM REPORT, UKPLU  For the subsequent items also the storinfo value will not be added fix it**    
- [x] ~~*Check DICTUPD flags, KEYCAT*~~  
- [ ] **Run For different current week**   
- [ ] **Dictionary Schema changes, fetching and updating from multiple tables**   
- [ ] Re-verify the Script  
- [ ] test for all the items in dictionary   
- [ ] Simulate run for the updated query and update the dctread func  
- [ ] Need to update market bit field, wadbit, wlmbit  
- [ ] 

27/06/2025

- [ ] **SYSTEM REPORT, UKPLU**   
- [ ] *Check DICTUPD flags, KEYCAT*  
- [ ] **Run For different current week**  
- [ ] **Dictionary Schema changes, fetching and updating from multiple tables**  
- [ ] Re-verify the Script  
- [ ] test for all the items in dictionary   
- [x] ~~Fix MinGen to EarlGen~~  
- [ ] Simulate run for the updated query and update the dctread func

26/06/2025

- [ ] **SYSTEM REPORT, UKPLU**   
- [ ] *Check DICTUPD flags, KEYCAT*  
- [ ] **Run For different current week**  
- [ ] **Dictionary Schema changes, fetching and updating from multiple tables**  
- [ ] Jana  
  - [x] ~~Main Script Explanation~~   
- [ ] Re-verify the Script  
- [x] ~~Test for local postgreslin~~

25/06/2025

- [ ] **SYSTEM REPORT, UKPLU**   
- [ ] *Check DICTUPD flags, KEYCAT*  
- [ ] **Run For different current week**  
- [ ] **Dictionary Schema changes, fetching and updating from multiple tables**  
- [ ] Jana  
  - [ ] Main Script Explanation   
- [ ] Re-verify the Script  
- [ ] 

24/06/2025

- [x] ~~**Jana**~~  
  - [x] ~~**price updates**~~  
  - [x] ~~**processhicones**~~  
- [ ] *Test Process Hicone , internally and check the Replacemoveprice*   
- [ ] *Test for what logic does the processhicones get executed*   
- [ ] Watch dictionary job design review  
- [ ] Implement and Test WEEK  36, first condition of the iritem  
- [x] ~~Prepare Country wise document ✨ (partially done, still needs to be reviewed)~~  
- [ ] **Dictionary Schema changes, fetching and updating from multiple tables**  
- [x] ~~**Implement the WEEK  36, first condition of the iritem  IF THE FIRST CONDITION SATISFIED and TEST ✨**~~  
- [ ] **SYSTEM REPORT, UKPLU**   
- [ ] *Check DICTUPD flags, KEYCAT*  
- [ ] **Run For different current week**

23/06/2025

- [x] ~~**Create a df where the discarded records are left and given a reason for the discard**~~   
- [ ] **Dictionary Schema changes, fetching and updating from multiple tables ✨**  
- [ ] **SYSTEM REPORT, UKPLU**   
- [ ] **Implement the WEEK  36, first condition of the iritem  IF THE FIRST CONDITION SATISFIED**  
- [ ] *Test and correct the issues*  
  - [ ] *KEYCAT, MFBCAT*  
  - [ ] *DICTUPD  known issue*  
  - [ ] *IMU*  
  - [x] ~~*Fix filler*~~  
  - [ ] *UNITPRICE [link](?tab=t.jukuq57dkj50)*  
- [ ] *Test Process Hicone , internally and check the Replacemoveprice*   
- [ ] *Test for what logic does the processhicones get executed ✨*  
- [ ] *Analyze Dict Price, process hicone for 10  20 minutes, and understand for why it will be executing*  
- [ ] *Check DICTUPD flags, KEYCAT*  
- [ ] **Run For different current week**  
- [x] ~~**jana  program**~~  
  - [x] ~~Dictionary Read~~  
  - [x] ~~Price updation logic~~ 

20/06/2025

- [ ] **Create a df where the discarded records are left and given a reason for the discard**   
- [ ] **Dictionary Schema changes, fetching and updating from multiple tables ✨**  
- [ ] *Test and correct the issues*  
  - [ ] *KEYCAT, MFBCAT*  
  - [ ] *DICTUPD  known issue*  
  - [ ] *IMU*  
  - [x] ~~*Fix filler*~~  
  - [ ] *UNITPRICE [link](?tab=t.jukuq57dkj50)*  
- [ ] *Test Process Hicone , internally and check the Replacemoveprice*   
- [ ] *Test for what logic does the processhicones get executed ✨*  
- [ ] *Analyze Dict Price, process hicone for 10  20 minutes, and understand for why it will be executing*  
- [ ] *Check DICTUPD flags, KEYCAT*  
- [ ] **Run For different current week**   
- [x] ~~Test Filter component~~



18/06/2025

- [ ] **Create a df where the discarded records are left and given a reason for the discard**   
- [x] ~~**add IRISTORE for joining store number  1 Logic STORMKT ✨**~~  
  - [x] ~~changing StoreNumber to two versions, one for coalescing , other for joining the tables and dropping  NEWSTORE*Temp , StoreNumber*Key  is used for joining table , Drop StoreNumber, Rename~~   
- [ ] **Dictionary Schema changes, fetching and updating from multiple tables**   
- [x] ~~*Analyze api parameters and flow parameters*~~  
- [ ] *Test and correct the issues*  
  - [ ] *KEYCAT, MFBCAT*  
  - [ ] *DICTUPD  known issue*  
  - [ ] *IMU*  
  - [x] ~~*Fix filler*~~  
  - [ ] UNITPRICE [link](?tab=t.jukuq57dkj50)  
- [ ] *Test Process Hicone , internally and check the Replacemoveprice*  
- [ ] *Test for what logic does the processhicones get executed*  
- [ ] *Analyze Dict Price, process hicone for 10  20 minutes, and understand for why it will be executing*  
- [ ] *Check DICTUPD flags, KEYCAT*  
- [x] ~~Backup~~

13/06/2025

- [ ] ***Run for different Week***  
  - [ ] *Check*  
- [x] ~~*Convert cluster to character*~~  
- [ ] *Backup*  
- [ ] *Analyze api parameters and flow parameters*  
- [ ] *Test and correct the issues*  
  - [ ] *KEYCAT, MFBCAT*  
  - [ ] *DICTUPD  known issue*  
  - [ ] *IMU*  
  - [ ] *Fix filler*  
  - [ ] UNITPRICE [link](?tab=t.jukuq57dkj50)  
- [ ] *Refactor Names in Scripts*  
- [ ] *Test Process Hicone , internally and check the Replacemoveprice*  
- [ ] *Test for what logic does the processhicones get executed*  
- [ ] *Analyze Dict Price, process hicone for 10  20 minutes, and understand for why it will be executing*  
- [ ] *Check DICTUPD flags, KEYCAT*  
- [x] ~~Test API, Parameterize~~

09/06/2025

- [ ] ***Run for different Week***  
  - [ ] *Check*  
- [x] ~~Convert cluster to character~~  
- [ ] Backup  
- [ ] Analyze api parameters and flow parameters  
- [ ] *Test and correct the issues*  
  - [ ] *KEYCAT, MFBCAT*  
  - [ ] *DICTUPD  known issue*  
  - [ ] *IMU*  
  - [ ] *Fix filler*  
- [ ] *Refactor Names in Scripts*  
- [ ] *Test Process Hicone , internally and check the Replacemoveprice*  
- [ ] *Test for what logic does the processhicones get executed*  
- [ ] Analyze Dict Price, process hicone for 10  20 minutes, and understand for why it will be executing  
- [ ] Check DICTUPD flags, KEYCAT  
- [x] ~~Do a thorough, store table understanding~~  
- [x] ~~Create a ZERO KEYED NEWITEM, MOVEOUT~~

08/06/2025

- [ ] *Run for different Week*  
- [ ] *Test and correct the issues*  
  - [ ] *OSYSTEM  6 , Null in actual*   
  - [x] ~~*NEWSTORE*~~  
  - [ ] *KEYCAT, MFBCAT*  
  - [ ] *DICTUPD  known issue*  
  - [ ] *IMU*  
- [x] ~~Test for dictwrite and dict update and~~   
- [x] ~~WHat is zero key item , new item   keycat OR mfbcat test using new item~~  
- [ ] Refactor Names in Scripts  
- [x] ~~Convert to New Dictionary Schema~~  
- [ ] 
- [ ] Update the discard record code  
- [ ] *Test Process Hicone , internally and check the Replacemoveprice*  
- [ ] *Give out Unit Tests , extract small pieces of code from the PL Logic make it into a component , write a documentation*   
  - [x] ~~*Test Before Predict and validate carefully*~~  
    - [x] ~~*Scaling and Unscaling MOVEDOLLARS*~~  
    - [x] ~~*record type from movement, record type movcomb and record type*~~ 

- [ ] *List out*  
  - [x] ~~*Test **Abbreviation*~~**   
  - [ ] *Find a dictionary entry that is newly added from weekdata and test it **description***  
  - [ ] *Test for what logic does the processhicones get executed*

06/06/2025

- [ ] *Run for different Week*  
- [ ] *Test Process Hicone , internally and check the Replacemoveprice*  
- [ ] *CHange names to standard*  
- [x] ~~*Complete the Documentation*~~  
- [ ] *Test and correct the issues*  
  - [ ] *OSYSTEM  6 , Null in actual*   
  - [ ] *NEWSTORE*  
  - [ ] *KEYCAT, MFBCAT*  
  - [ ] *DICTUPD  known issue*  
  - [x] ~~*MOVEDOLLARS, MOVEUNITS, SAVEDOLLARS  Deal with decimals*~~  
- [ ] *Give out Unit Tests , extract small pieces of code from the PL Logic make it into a component , write a documentation*   
  - [x] ~~*Test Before Predict and validate carefully*~~  
    - [x] ~~*Scaling and Unscaling MOVEDOLLARS*~~  
    - [x] ~~*record type from movement, record type movcomb and record type*~~ 

- [ ] *List out*  
  - [ ] *Test **Abbreviation***   
  - [ ] *Find a dictionary entry that is newly added from weekdata and test it **description***  
  - [ ] *Test for what logic does the processhicones get executed*  
- [x] ~~*Track the git history of a file*~~  
- [x] ~~*Explore output parameters*~~  
- [x] ~~*How Spark , juptyer kernel is working, what is notebook*~~

05/06/2025

- [ ] Run for different Week  
- [ ] *Test Process Hicone , internally and check the Replacemoveprice*  
- [ ] *CHange names to standard*  
- [x] ~~*Complete the Documentation*~~  
- [ ] Test and correct the issues  
  - [ ] OSYSTEM  6 , Null in actual   
  - [ ] NEWSTORE  
  - [ ] KEYCAT, MFBCAT  
  - [ ] DICTUPD  known issue  
  - [ ] MOVEDOLLARS, MOVEUNITS, SAVEDOLLARS  Deal with decimals  
- [ ] *Give out Unit Tests , extract small pieces of code from the PL Logic make it into a component , write a documentation*   
  - [x] ~~*Test Before Predict and validate carefully*~~  
    - [x] ~~*Scaling and Unscaling MOVEDOLLARS*~~  
    - [x] ~~*record type from movement, record type movcomb and record type*~~ 

- [ ] *List out*  
  - [ ] *Test **Abbreviation***   
  - [ ] *Find a dictionary entry that is newly added from weekdata and test it **description***  
  - [ ] *Test for what logic does the processhicones get executed*  
- [x] ~~*Track the git history of a file*~~  
- [ ] *Explore output parameters*  
- [ ] *How Spark , juptyer kernel is working, what is notebook*

04/06/2025

- [ ] Run for different Week  
- [x] ~~GIve files to testing team~~  
- [ ] Check for TOTAL UPC check for client files  
- [ ] Test and correct the issues  
  - [ ] OSYSTEM  6 , Null in actual   
  - [ ] NEWSTORE  
  - [ ] KEYCAT, MFBCAT  
  - [ ] MOVEDOLLARS, MOVEUNITS, SAVEDOLLARS  Deal with decimals  
- [ ] *Test Process Hicone , internally and check the Replacemoveprice*  
- [ ] *CHange names to standard*  
- [ ] *Complete the Documentation*  
- [ ] *Test  IRITEM.MOVEUNITS*   
- [ ] *Give out Unit Tests , extract small pieces of code from the PL Logic make it into a component , write a documentation*   
  - [x] ~~*Test Before Predict and validate carefully*~~  
    - [x] ~~*Scaling and Unscaling MOVEDOLLARS*~~  
    - [x] ~~*record type from movement, record type movcomb and record type*~~ 

- [ ] *List out*  
  - [ ] *Test **Abbreviation***   
  - [ ] *Find a dictionary entry that is newly added from weekdata and test it **description***  
  - [ ] *Test for what logic does the processhicones get executed*  
- [ ] *Track the git history of a file*  
- [ ] *Explore output parameters*  
- [ ] *How Spark , juptyer kernel is working, what is notebook*

03/06/2025

- [ ] Test Process Hicone , internally and check the Replacemoveprice  
- [ ] CHange names to standard  
- [ ] Complete the Documentation  
- [ ] Test  IRITEM.MOVEUNITS   
- [ ] *Give out Unit Tests , extract small pieces of code from the PL Logic make it into a component , write a documentation*   
  - [x] ~~*Test Before Predict and validate carefully*~~  
    - [x] ~~*Scaling and Unscaling MOVEDOLLARS*~~  
    - [x] ~~*record type from movement, record type movcomb and record type*~~ 

- [ ] *List out*  
  - [ ] *Test **Abbreviation***   
  - [ ] *Find a dictionary entry that is newly added from weekdata and test it **description***  
  - [ ] *Test for what logic does the processhicones get executed*  
- [ ] Track the git history of a file  
- [ ] Explore output parameters  
- [ ] How Spark , juptyer kernel is working, what is notebook



02/06/2025

- [x] ~~**Check why resultsdf generation not changed to valid number**~~  
- [x] ~~Add Inferences for record discarding~~   
- [ ] Test Process Hicone , internally and check the Replacemoveprice  
- [x] ~~Check generation differences output to exact output~~  
- [ ] CHange names to standard  
- [x] ~~*Implement the Cleaning process during last steps , verify once*~~  
- [ ] *Give out Unit Tests , extract small pieces of code from the PL Logic make it into a component , write a documentation*   
  - [x] ~~*Test Before Predict and validate carefully*~~  
    - [x] ~~*Scaling and Unscaling MOVEDOLLARS*~~  
    - [x] ~~*record type from movement, record type movcomb and record type*~~ 

- [ ] *List out*  
  - [ ] *Test **Abbreviation***   
- [ ] Track the git history of a file  
- [ ] Explore output parameters  
  - [ ] *Find a dictionary entry that is newly added from weekdata and test it **description***  
  - [ ] *Test for what logic does the processhicones get executed*  
- [x] ~~Add the STOREHASH from Untitiled and add a version to it~~   
- [ ] Track the git history of a file  
- [ ] Explore output parameters

01/05/2025

- [ ] ~~Open postgres script, use sql to test it with new db , check count~~   
- [x] ~~Open Putty , check the count  and create a new table~~   
- [x] ~~FIrst Analyze the program where we are using it , First copy the content to vscode and then commit and then edit with corresponding columns~~  
- [ ] ~~Test~~  
  - [ ] ~~DIctionary Read , Write, update~~   
  - [ ] ~~Test it with process dictionary~~   
  - [ ] ~~Check gpt for testing it easy way~~   
- [x] ~~Price Logic with GPT,~~   
- [x] ~~*Also check the price logic with GPT and check end product*~~  
- [ ] *Implement the Cleaning process during last steps , verify once*  
- [ ] *Give out Unit Tests , extract small pieces of code from the PL Logic make it into a component , write a documentation*   
  - [ ] *Test Before Predict and validate carefully*  
    - [x] ~~*Scaling and Unscaling MOVEDOLLARS*~~  
    - [x] ~~*record type from movement, record type movcomb and record type*~~ 

- [ ] *List out*  
  - [ ] *Test **Abbreviation***   
  - [ ] *Find a dictionary entry that is newly added from weekdata and test it **description***  
  - [ ] *Test for what logic does the processhicones get executed*  
- [ ] Add the STOREHASH from Untitiled and add a version to it 

30/05/2025

- [ ] Add log to the main dict step  
- [x] ~~Retreive the 5000 items and store it and do a for loop and call the dictionary individually~~   
- [x] ~~Retrieve the remaining and check its upc and find fuzzy matches~~  
- [x] ~~Test whether the fields are going parsed, log and test the sql query which is going to hit, and make changes to all the funcitons~~  
- [ ] Also check the price logic with GPT and check end product  
- [ ] Implement the Cleaning process during last steps , verify once  
- [ ] *Give out Unit Tests , extract small pieces of code from the PL Logic make it into a component , write a documentation*   
  - [ ] *Test Before Predict and validate carefully*  
    - [x] ~~*Scaling and Unscaling MOVEDOLLARS*~~  
    - [x] ~~*record type from movement, record type movcomb and record type*~~ 

- [ ] *List out*  
  - [ ] *Test **Abbreviation***   
  - [ ] *Find a dictionary entry that is newly added from weekdata and test it **description***  
  - [ ] *Test for what logic does the processhicones get executed*

29/05/2025

- [ ] *Give out Unit Tests , extract small pieces of code from the PL Logic make it into a component , write a documentation*   
  - [ ] *Test Before Predict and validate carefully*  
    - [x] ~~*Scaling and Unscaling MOVEDOLLARS*~~  
    - [x] ~~*record type from movement, record type movcomb and record type*~~ 

- [ ] *List out*  
  - [ ] *Test **Abbreviation***   
  - [ ] *Find a dictionary entry that is newly added from weekdata and test it **description***  
  - [ ] *Test for what logic does the processhicones get executed*

28/05/2025

- [ ] *Give out Unit Tests , extract small pieces of code from the PL Logic make it into a component , write a documentation*   
  - [ ] *Test Before Predict and validate carefully*  
    - [ ] *Scaling and Unscaling MOVEDOLLARS*  
    - [x] ~~*record type from movement, record type movcomb and record type*~~ 

- [ ] *List out*  
  - [ ] *Test **Abbreviation***   
  - [ ] *Find a dictionary entry that is newly added from weekdata and test it **description***  
  - [ ] *Test for what logic does the processhicones get executed*  
  - [x] ~~Use GPT to validate the conditions before that~~

27/05/2025

- [x] ~~Get New Item files~~  
- [ ] Give out Unit Tests , extract small pieces of code from the PL Logic make it into a component , write a documentation   
  - [ ] Test Before Predict and validate carefully  
    - [x] ~~Valid Store numbers~~  
    - [x] ~~Valid UPC, Checks for wild UPC values~~  
    - [x] ~~StoreNumber Correction, correct and verify with NEWSTORE~~  
    - [ ] Scaling and Unscaling MOVEDOLLARS  
    - [ ] record type from movement, record type movcomb and record type   
    - [ ] List out  
  - [ ] Test **Abbreviation**   
  - [ ] Find a dictionary entry that is newly added from weekdata and test it **description**  
  - [ ] Test for what logic does the processhicones get executed  
  - [x] ~~Get New weekdata files~~  
- [ ] Use GPT to validate the conditions before that

26/05/2025

- [x] ~~Get New Item files~~  
- [ ] Give out Unit Tests , extract small pieces of code from the PL Logic make it into a component , write a documentation   
  - [ ] Test Before Predict and validate carefully  
  - [ ] Test **Abbreviation**   
  - [ ] Find a dictionary entry that is newly added from weekdata and test it **description**  
  - [ ] Test for what logic does the processhicones get executed  
  - [ ] Get New weekdata files  
- [ ] Use GPT to validate the conditions before that

23/05/2025

- [x] ~~Implement LAC code~~  
- [x] ~~*update*~~  
- [x] ~~*Storinfo hash,*~~   
- [x] ~~*Test update, and write once again*~~  
- [x] ~~*Deal with Ideal Unit Price*~~  
- [x] ~~*Need to add commit() at last*~~   
- [x] ~~*Try at which point collect() is breaking*~~  
- [ ] *Check the formulat column in is components for which case we set it to N, Y*  
- [x] ~~*Take a backup of the scripts*~~  
- [ ] Extract Weekdata, compare weekdata with movcomb see for any changes  
- [ ] Watch about git, practice i

22/05/2025

- [x] ~~Need to correctly set DescCompl during intitilaize and dctread step~~   
- [x] ~~abbrev()~~  
- [ ] *update*  
- [ ] *Storinfo hash,*   
- [ ] *Test update, and write once again*  
- [ ] *Deal with Ideal Unit Price*  
- [ ] *Need to add commit() at last*   
- [ ] Try at which point collect() is breaking  
- [ ] Check the formulat column in is components for which case we set it to N, Y  
- [x] ~~Check with records missing in DICT.failed for missing 0 generation~~  
- [ ] Take a backup of the scripts

21/05/2025

- [x] ~~*Move out , new item file*~~  
- [ ] abbrev()  
- [ ] *update*  
- [ ] *Storinfo hash,*   
- [ ] *Test update, and write once again*  
- [ ] *Deal with Ideal Unit Price*  
- [ ] *Need to add commit() at last*   
- [ ] Try at which point collect() is breaking  
- [ ] Check the formulat column in is components for which case we set it to N, Y  
- [ ] Check with records missing in DICT.failed for missing 0 generation

20/05/2025

- [x] ~~Test processhicone logic~~  
- [ ] *Move out , new item file*  
- [ ] abbrev()  
- [ ] *update*  
- [ ] *Storinfo hash,*   
- [ ] *Test update, and write once again*  
- [ ] *Deal with Ideal Unit Price*  
- [ ] *Need to add commit() at last*   
- [ ] Try at which point collect() is breaking  
- [x] ~~Add global typing for Dict~~  
- [ ] Check the formulat column in is components for which case we set it to N, Y



19/05/2025

- [x] ~~Implement the processhicones~~  
- [ ] Move out , new item file  
- [ ] Storinfo hash,   
- [ ] Test update, and write once again  
- [x] ~~Check price updation logic~~

18/05/2025

- [x] ~~Implement Initialize , Write Dict~~  
- [x] ~~For write dict first we will print the whole data~~  
- [x] ~~Extract sample data set for 20 items , with 10 (  3,3, 2 , 1, 1 sets of valid upcs, 10 invalid upcs (4,2,2,1)~~  
- [x] ~~PROCESSHICONES label, 5pm~~  
- [ ] Deal with Ideal Unit Price  
- [ ] Processhicones and dictupdate logic  
- [ ] Need to add commit() at last   
- [ ] Need to test storinfo hash

13/05/2025

12/05/2025

- [ ] Complete in IS before dictionary price updation

07/05/2025

- [x] ~~*Complete Documention of upto the step before dictionary reading*~~  
- [ ] *Complete Dictionary Reading 0 and 5*  
- [ ] *Add all the storinfo and variable columns needed in the predict step*  
- [ ] Add Invalid Store BADSTORE , log or use a script to filter the output , ZERCOUNT  
- [ ] Complete upto Dictionary Updation before processhicones  
- [x] ~~Create Keycat table~~

06/05/2025

- [x] ~~Look into hicone logic~~  
  - [x] ~~Step 1~~  
  - [x] ~~Step 2~~  
- [x] ~~Integrate with database, and make it a separate component and interact it with~~   
- [ ] Complete documentation, of upto the step before dictionary reading involved  after 9pm  
- [ ] Complete dictionary read Logic that is error code 0 and 5 

05/05/2025

- [x] ~~Completed first part dict updation  created abbrev function~~  
- [x] ~~Secondary price updation~~  
- [ ] Look into hicone logic  
- [ ] Implement it in docs   
- [ ] Convert it to pyspark and IS

03/05/2025

- [ ] Analyze price updation logic  
- [ ] Docs and update notes  
- [ ] And try to come up with implementation part

02/05/2025

- [x] ~~Complete dictionary updation  2100~~  
- [x] ~~Upto HICONE ,~~   
- [x] ~~Add storinfo fields in the pre dict step itself~~  
- [ ] Docs and update notes

01/05/2025

- [x] ~~Implement the last part in IS~~   
- [ ] Analyze carefully and implement the corresponding spark code when 0 : when 5 : Process Hicones  day   
- [ ] Write Docs and update notes

30/04/2025

- [x] ~~Look for specific chains in stormkt~~

29/04/2025

- [ ] ~~Create a standalone dictionary Read Component~~  
- [ ] Remove masterrec logics  
- [ ] The remaining logic  parse upto 400 lines  
- [ ] Try to implement simple reading and writing 

28/04/2025

- [x] ~~Verify the storinfo type, add storinfo store, and add sotringo footprintsubtract,~~   
- [ ] Remove masterrec logics  
- [ ] The remaining logic  parse upto 400 lines  
- [ ] The script inside script i can add dictionary logic   
- [ ] Analyze the dictionary updation main logic 

25/04/2025

- [ ] Analyze the isUPCFound Condition, HICONE,  
- [ ] Unscaled part, movedollars, is valid market, filter out valid market and drop the master rec from main master dataframe   
- [ ] Country PLU  
- [x] ~~Dictionary fields~~    
- [x] ~~Validate the error checks, implement~~   
- [x] ~~Compare with MOVCOMB, validate results~~

```javascript
IF IRITEM.MOVE_DOLLARS = 0 &              /* CHECK MOVEMENT */
        IRITEM.MOVE_LBS = 0 &
        IRITEM.MOVE_UNITS = 0 THEN DO;
        STORINFO(STORINFO_INDEX).ZER_COUNT =   /* INCREMENT COUNTER */
           STORINFO(STORINFO_INDEX).ZER_COUNT + 1;
        GOTO READ_NEXT;                        /* SKIP THIS REC */
        END; /* IF IRITEM.MOVE_DOLLARS = 0 & ... */
```

23/04/2025

- [ ] Convert Script to IS  
  - [x] ~~STORINFO~~   
  - [ ] Country PLU  
- [ ] Complete bscan- hicone 2200

21/04/2025

- [ ] Convert to spark, and IS  
- [ ] Complete upto process hicones  2200  
- [ ] Make a doc related to what processes can be converted to Pyspark  IS  
- [ ] Indexed db, find the row based ont he already available output 

20/04/2025

17/04/2025

- [ ] Parse the codebase and add docs  
- [ ] Redesign the doc  
- [ ] Come up with a database design  
- [ ] Need to change the movein parsing , sub attributes naming , like footprint.substract, footprint.pluxlated

11/04/2025

- [ ] DICTWK  
  - [ ] Implement the hashing of the storinfo part

10/04/2025

- [ ] DICTWK  
  - [ ] Implement the hashing of the storinfo part  
- [x] ~~Try to trigger flow using api, or api trigger~~

09/04/2025

- [x] ~~Implemented the validation code in IS, working fine~~

08/04/2025

- [ ] *DICTWK*    
  - [ ] *MAINLINE(1600  2100  create doc, and analyze it and interpret it in code*  
  - [ ] *MAINLINE(2000)  3100 line*  
- [ ] *About*   
  - [ ] *Snippets*  
  - [ ] *API*  
  - [ ] *Database*  
  - [ ] *Calling snippets*   
- [ ] *Dependency injection*  
- [ ] *Find a way to exit, log status, the code to make it similar to pl/1*

08/04/2025

- [ ] *DICTWK*    
  - [ ] *MAINLINE(1600  2100  create doc, and analyze it and interpret it in code*  
  - [ ] *MAINLINE(2000)  3100 line*  
- [ ] *About*   
  - [ ] *Snippets*  
  - [ ] *API*  
  - [ ] *Database*  
  - [ ] *Calling snippets*   
- [ ] *Dependency injection*  
- [ ] *Find a way to exit, log status, the code to make it similar to pl/1*  
- [x] ~~Implement the same in is~~

07/04/2025

- [ ] *DICTWK*    
  - [x] ~~*MAINLINE(1600  2100  create doc, and analyze it  (Completed upto 1650 lines in code)*~~  
  - [ ] *MAINLINE(2000)  3100 line*  
- [ ] About   
  - [ ] Snippets  
  - [ ] API  
  - [ ] Database  
  - [ ] Calling snippets   
- [x] ~~Creating a abstracted design of the~~   
- [ ] Dependency injection  
- [ ] Find a way to exit, log status, the code to make it similar to pl/1  

- [x] ~~Watch KT video~~   
  - [x] ~~1 and 2 (2 incomplete)~~  
  - [x] ~~2 and 3 and IS  and 4~~  
    - [x] ~~Census Flow Diagram~~  
    - [x] ~~JCL Videos~~  
  - [x] ~~Watch 5 and 6 repeatedly~~  
  - [ ] Check Flow chart and its program   
  - [x] ~~Watch Census 1 and go to dictionary job~~  
  - [x] ~~Casual Processing 1 and Casual Processing 2~~  
- [ ] Mar 4, 2025 11:30 PM  Aggregating functions, map reduce, mongo db aggregates, sql aggregates   
- [ ] [https://regex101.com/quiz](https://regex101.com/quiz)

12/03/2025  
⌛

- [x] ~~Watch IS KT Video Recording~~ 	  
- [x] ~~What is byte , binary analyze~~  
- [x] ~~Analyze JCL and do file analysis  cgpt~~ 

Analyze Code of JCL , and PPL

- [x] ~~Create a simple IS flow~~



#### 17/03/2025

- [x] ~~Analyze the JCL and make changes to the flow~~   
- [ ] Analyze DICTWK2 and try to analyze the External Dependencies   
- [x] ~~How movement record are checked and how it is given as movcomb~~  
- [x] ~~How to publish content in IS~~

18/03/2025

- [x] ~~Check Once again the IRITEM structure,  ask Dh about the script~~   
- [ ] *Analyze DICTWK2 and try to analyze the External Dependencies*   
- [x] ~~Verify and Modify the RAW file parser (Changed from str to input for the other variables)~~  
- [x] ~~Complete 2 python~~  
- [ ] Re verify output of the parser with the screenshot



#### 19/03/2025

- [x] ~~*Analyze DICTWK2 and try to analyze the External Dependencies*~~   
- [x] ~~Re verify output of the parser with the screenshot~~  
- [ ] Analyze why OGENERATION is not coming as 1  
- [x] ~~Look into CENDICT.PROCDEURE and gain insights~~  
- [ ] Change sort to script wise sort

20/03/2025

- [x] ~~PLPROG  Phase I~~  
- [ ] PLPROG  Phase II  
- [ ] Analyze CENDICT  and put notes   
- [x] ~~*Change sort to script wise sort*~~  
- [x] ~~Watch 5 basics structure of PLProg~~  
- [ ] *Analyze why OGENERATION is not coming as 1*

21/03/2025

- [x] ~~PLPROG  Phase II  (Seperated into further tasks in next day)~~  
- [x] ~~Fix the DF Error~~  
- [ ] Experiment with saveResults option  
- [ ] Experiment with creating output file   
- [x] ~~*Analyze why OGENERATION is not coming as 1*~~

24/03/2025

- [ ] Deduce / Draw Flows for the PL Program  
- [ ] Convert PL Program to flow script    
- [ ] *Experiment with saveResults option*  
- [ ] *Experiment with creating output file*   
- [x] ~~How to handle arguments  parameters and set some state to the flow~~ 

25/03/2025

- [ ] Convert PL Program to flow script    
  - [x] ~~**Data Definition Part**~~  
  - [ ] Program Implementation  
- [ ] **Deduce / Draw Flows for the PL Program**  
- [ ] 
- [ ] *Experiment with saveResults option*  
- [ ] *Experiment with creating output file* 

2703/2025

- [ ] Read Records from MOVEIN file

28/03/2025

- [x] ~~Work with the difference between DCTDATA and DICTRECL and DICT~~  
- [x] ~~Analyze STORINFO  pointer~~

02/04/2025

- [ ] STORINFO  create   
  - [ ] Keycatin  keycat table  
- [x] ~~Look into DICT.READ, DICT.WRITE~~  
- [ ] ~~Git advanced~~  
- [ ] Draw flows for the program as a diagram   
- [ ] ~~MSEM~~

03/04/2025

- [ ] *STORINFO  create*   
  - [ ] *Keycatin  keycat table*  
- [ ] *Draw flows for the program as a diagram*   
- [ ] DICTWK    
  - [ ] MAINLINE(1650)  3100 line