README AJHG 2009 DOI: 10.1016/j.ajhg.2009.03.011
August 2018 v1
AJ Myers

1. files:

364s_8650_transcripts_analysis.txt
adgwas.map.zip
adgwas.ped-1.zip
annnot_det_rate_manifest.txt
gids.list.zip
residuals.pheno.zip
samples.covar.zip


2. descriptors: 
 
364s_8650_transcripts_analysis.txt

	Tab delimited file of rank-invariant normalized intensities for expression data for 
	the 364 individuals used in our analysis. Transcripts that were detected in less than 
	90% of cases or 90% of controls are not included. Data is not log10 transformed. 
	Transcripts are listed in column A by their illumina target ID, which contains the 
	GI accession number for each transcript. Samples are listed in row A and identifiers 
	correspond to those given in the covariate information. Any intensity where the 
	Illumina detection score was <0.99 was coded as NaN. 
	
	NOTE THESE FILES CONTAIN WGACON 120 WHICH IS NOT IN THE GEO FILE. 
	IT WAS SUBSEQUENTLY FOUND TO BE IDENTICAL TO WGAAD 247. 
 	WGAAD 247 IS THE RIGHT IDENTIFIER.

adgwas.map.zip
	
	PMap file gives the position of each SNP on the chromosomes relative to the Human 
	Genome Build 36 is included and denoted by the extension .map. The pmap file is in 
	the 4 column format which is described at 
	http://pngu.mgh.harvard.edu/~purcell/plink/data.shtml#map.

adgwas.ped-1.zip
	
	Genotypes calls from 502,627 SNPs on the 364 samples are given as well as anonymous 
	individual identifiers for each sample. Data is not filtered for call rates, allele 
	frequencies or Hardy Weinberg equilibrium. Data is not imputed. Pedigree file is 
	denoted by the extension .ped. File is in Linkage Pedigree format which is described at 
	http://pngu.mgh.harvard.edu/~purcell/plink/data.shtml#ped. Paternal ID and Maternal ID 
	(columns C and D) on the file are marked as 0, since none of our samples are related. 
	Alleles are coded as A, C, G, T and missing=0.  Alleles are coded by Affymetrix calls 
	not dbSNP.
	
annnot_det_rate_manifest.txt	
	
	Text file of information of each of the 8650 transcripts. Column identifiers are 
	in line 1. File includes average detection rates for cases and controls for each 
	transcript.  
	
gids.list.zip

	Tab Delimited .txt file giving the GI identifiers for each column of the residual 
	expression data file.  Column 3 of the RESIDUAL EXPRESSION DATA file corresponds to 
	the first GI given in this map and so on.
	
residuals.pheno.zip	
	
	Tab delimited .txt file of residual corrected profiles for each individual for each 
	transcript. Corrections were made for gender, APOE status, age at death, 
	cortical region, day of expression hybridization, institute source of sample, 
	postmortem interval, and transcript detection rate using R (see publication). 
	File is in the format of an alternate phenotypes file described at 
	http://pngu.mgh.harvard.edu/~purcell/plink/data.shtml#pheno. 
	
	NOTE THAT MISSING VALUES (NaN on other files) ARE CODED AS -9.0.

samples.covar.zip	
	Group and member names correspond to individual identifiers given in the pedigree files. 
	All covariates used in the analysis are listed. Columns are as follows:
	
	Column 1    Group identifier
	Column 2    Individual identifier
	Column 3    Diagnosis (1=unaffected, 2=affected)
	Column 4    Age
	Column 5    APOE
	Column 6    Region (1=frontal, 2=parietal, 3=temporal, 4=cerebellar)
	Column 7    PMI
	Column 8    Site
	Column 9    Hybridization Date



	
 

 	
 	
 	