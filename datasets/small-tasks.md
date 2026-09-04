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
