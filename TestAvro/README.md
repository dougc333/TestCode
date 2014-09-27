TestAVROIBM: from web article
TestAVROSimple: Avro for spark
TestParquet

Given a data record, say Person(String name, int age, Addresss address) there are many different ways to store this in HDFS and protocols for serializing the Person object when it is transported to other nodes in a cluster. 

For distributed computing using M/R there is a shuffle stage where objects are serialized and sent across the network to various reducers. Using Java Serialization was too slow:(link to google protobuf)

Avro: JSON style schema definition. 
Parquet: Column style schema

