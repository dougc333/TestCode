Parquet is useful for certain types of queries over large datasets. The idea is to store your data records using parquet which groups data into row and column groups. 
This grouping has a custom serialization format which speeds up large scale query performance. 
Parquet is a column specific schema definition. The concept for Parquet comes from Google: 

The idea is instead of reading records from disk and recreating each object in memory to do a query on columns, 
we minimize the disk accessess if we group columns together in diskblocks so a disk read fetches multiple records
at a time to minimize disk transfers. 

This is only valuable for certain situations


