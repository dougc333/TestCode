input: lookup.csv, makedataforindex.py, create directory testindex
output: will create file names with rxcui as file name all under testindex

creates ~351k files under testindex
this is too many for solr to index
create 9 directories 

> mkdir [0..9]files
move the files starting with 1* to directory 1files, etc.... for all 9 directories

