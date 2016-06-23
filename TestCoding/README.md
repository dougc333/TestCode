med-sample.json
clinical.sqlite 

To create the search index
1) install solr-6.X; make sure jdk-1.8 or higher is installed. Else you will get an unrelated error message about solr not being able to write to solr.log

2) upload clinical.sqlite and create file lookup.csv with ... 

3) run makedataforindex.py from lookup.csv




