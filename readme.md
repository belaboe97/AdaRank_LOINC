
##Readme LOINC Ranking Project

This is a fork of githubuser rueychang https://github.com/rueycheng/AdaRank

### General Information: 
The Loinc Folder consists of various steps taken in order to make the lsitwisem approach:
	-labelprep: Scripts to do an automated labeling and extension of given LOINC dataset
	- MQ2007: Benchmark Dataset for ranking with over 40 Parameters (works with implemented AdaRank Library @rueycheng
	- resources: usefull papers about AdaRank and Letor 4 
	- results: results of the validation dataset after training AdaRank

	-Files:
	- test.py, utils.py ,metrics.py => part of reuycheng fork of AdaRank algorithm implementation
	- loinc_dataset_original, loinc_dataset_extended => Basic and modified version of loinc dataset
	- IPYNB File for preprocessing data

1. Installation: 
    	- pandas
	- numpy
    	- nltk 
	- os
	- re 
	- math 
	- spacy
	- sklearn
2. (files alread included) 
	- navigate to the folder and start jupyter notebook
	- Run Preprocess Dataset in order to achive files for AdaRank Algorithm implemented by @rueycheng


## These are the following batch commands for evaluating the results: 

["glucose in blood","bilirubin in plasma","White blood cells count"]
Query 1: Glucose in Blood 
_________________________________
Org_DS -> python test.py data/original_ds/q1/train.txt data/original_ds/q1/test.txt data/original_ds/q1/vali.txt -o=results/original_ds/gib.txt
Ext_DS -> python test.py data/extend_ds/q1/train.txt data/extend_ds/q1/test.txt data/extend_ds/q1/vali.txt -o=results/extend_ds/gib.txt

Query 2: bilirubin in plasma
_________________________________
Org_DS -> python test.py data/original_ds/q2/train.txt data/original_ds/q2/test.txt data/original_ds/q2/vali.txt -o=results/original_ds/bip.txt
Ext_DS -> python test.py data/extend_ds/q2/train.txt data/extend_ds/q2/test.txt data/extend_ds/q2/vali.txt -o=results/extend_ds/bip.txt

Query 3: White blood cells count 
_________________________________
Org_DS -> python test.py data/original_ds/q3/train.txt data/original_ds/q3/test.txt data/original_ds/q3/vali.txt -o=results/original_ds/wbcc.txt
Ext_DS -> python test.py data/extend_ds/q3/train.txt data/extend_ds/q3/test.txt data/extend_ds/q3/vali.txt -o=results/extend_ds/wbcc.txt


## These commands are usefull to run the Letor Benchmark Ranking Dataset:
	-python test.py MQ2007/Fold1/{train,vali,test}.txt
	- More Information: https://github.com/rueycheng/AdaRank/issues/1
