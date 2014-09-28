sbt project for spark
run sbt/bin/sbt 
>package
>run

manually install the spark streaming jar in the sbt. Build from source, manually install in ivy cache

For some reason I also copied the project to /usr/lib/spark. Can't remember why. 

2 programs in SimpleApp.scala

/*** SimpleApp.scala ***/
import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._

object SimpleApp {
  def main(args: Array[String]) {
    val logFile = "/usr/lib/spark/README.md" // Should be some file on your system
    val sc = new SparkContext("local", "Simple App", "/usr/lib/spark",
      List("target/scala-2.10/simple-project_2.10-1.0.jar"))
    val logData = sc.textFile(logFile, 2).cache()
    val numAs = logData.filter(line => line.contains("a")).count()
    val numBs = logData.filter(line => line.contains("b")).count()
    println("Lines with a: %s, Lines with b: %s".format(numAs, numBs))
    sc.stop()
  }
}



first run sbt/bin/sbt package. 
source file is copied to: ~/.sbt/0.13/staging/... 

[dc@localhost spark]$ sbt/bin/sbt
[info] Loading project definition from /home/dc/.sbt/0.13/staging/694e1cb1ecb12bfcaec2/spark/project
[info] Set current project to Simple Project (in build file:/usr/lib/spark/)


[dc@localhost spark]$ sbt/bin/sbt run
[info] Loading project definition from /home/dc/.sbt/0.13/staging/694e1cb1ecb12bfcaec2/spark/project
[info] Set current project to Simple Project (in build file:/usr/lib/spark/)
[info] Running SimpleApp 
SLF4J: Class path contains multiple SLF4J bindings.
SLF4J: Found binding in [jar:file:/home/dc/.sbt/0.13/staging/694e1cb1ecb12bfcaec2/spark/lib/slf4j-log4j12-1.7.2.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [jar:file:/home/dc/.ivy2/cache/org.slf4j/slf4j-log4j12/jars/slf4j-log4j12-1.7.5.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
SLF4J: Actual binding is of type [org.slf4j.impl.Log4jLoggerFactory]
14/09/27 17:13:11 INFO Utils: Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
14/09/27 17:13:11 WARN Utils: Your hostname, localhost.localdomain resolves to a loopback address: 127.0.0.1; using 192.168.171.1 instead (on interface vmnet8)
14/09/27 17:13:11 WARN Utils: Set SPARK_LOCAL_IP if you need to bind to another address
14/09/27 17:13:12 INFO Slf4jLogger: Slf4jLogger started
14/09/27 17:13:12 INFO Remoting: Starting remoting
14/09/27 17:13:13 INFO Remoting: Remoting started; listening on addresses :[akka.tcp://spark@192.168.171.1:58083]
14/09/27 17:13:13 INFO Remoting: Remoting now listens on addresses: [akka.tcp://spark@192.168.171.1:58083]
14/09/27 17:13:13 INFO SparkEnv: Registering BlockManagerMaster
14/09/27 17:13:13 INFO DiskBlockManager: Created local directory at /tmp/spark-local-20140927171313-43cf
14/09/27 17:13:13 INFO MemoryStore: MemoryStore started with capacity 588.8 MB.
14/09/27 17:13:13 INFO ConnectionManager: Bound socket to port 55921 with id = ConnectionManagerId(192.168.171.1,55921)
14/09/27 17:13:13 INFO BlockManagerMaster: Trying to register BlockManager
14/09/27 17:13:13 INFO BlockManagerMasterActor$BlockManagerInfo: Registering block manager 192.168.171.1:55921 with 588.8 MB RAM
14/09/27 17:13:13 INFO BlockManagerMaster: Registered BlockManager
14/09/27 17:13:13 INFO HttpServer: Starting HTTP Server
14/09/27 17:13:13 INFO HttpBroadcast: Broadcast server started at http://192.168.171.1:37086
14/09/27 17:13:13 INFO SparkEnv: Registering MapOutputTracker
14/09/27 17:13:13 INFO HttpFileServer: HTTP File server directory is /tmp/spark-d3268d54-b4f8-4b84-98af-648e5986beef
14/09/27 17:13:13 INFO HttpServer: Starting HTTP Server
14/09/27 17:13:14 INFO SparkUI: Started Spark Web UI at http://192.168.171.1:4040
14/09/27 17:13:14 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
14/09/27 17:13:15 INFO SparkContext: Added JAR target/scala-2.10/simple-project_2.10-1.0.jar at http://192.168.171.1:57638/jars/simple-project_2.10-1.0.jar with timestamp 1411863195200
14/09/27 17:13:15 INFO MemoryStore: ensureFreeSpace(152694) called with curMem=0, maxMem=617427763
14/09/27 17:13:15 INFO MemoryStore: Block broadcast_0 stored as values to memory (estimated size 149.1 KB, free 588.7 MB)
14/09/27 17:13:16 INFO FileInputFormat: Total input paths to process : 1
14/09/27 17:13:16 INFO SparkContext: Starting job: count at SimpleApp.scala:11
14/09/27 17:13:16 INFO DAGScheduler: Got job 0 (count at SimpleApp.scala:11) with 2 output partitions (allowLocal=false)
14/09/27 17:13:16 INFO DAGScheduler: Final stage: Stage 0 (count at SimpleApp.scala:11)
14/09/27 17:13:16 INFO DAGScheduler: Parents of final stage: List()
14/09/27 17:13:16 INFO DAGScheduler: Missing parents: List()
14/09/27 17:13:16 INFO DAGScheduler: Submitting Stage 0 (FilteredRDD[2] at filter at SimpleApp.scala:11), which has no missing parents
14/09/27 17:13:16 INFO DAGScheduler: Submitting 2 missing tasks from Stage 0 (FilteredRDD[2] at filter at SimpleApp.scala:11)
14/09/27 17:13:16 INFO TaskSchedulerImpl: Adding task set 0.0 with 2 tasks
14/09/27 17:13:16 INFO TaskSetManager: Starting task 0.0:0 as TID 0 on executor localhost: localhost (PROCESS_LOCAL)
14/09/27 17:13:16 INFO TaskSetManager: Serialized task 0.0:0 as 1690 bytes in 13 ms
14/09/27 17:13:16 INFO Executor: Running task ID 0
14/09/27 17:13:16 INFO Executor: Fetching http://192.168.171.1:57638/jars/simple-project_2.10-1.0.jar with timestamp 1411863195200
14/09/27 17:13:16 INFO Utils: Fetching http://192.168.171.1:57638/jars/simple-project_2.10-1.0.jar to /tmp/fetchFileTemp1974113250158011789.tmp
14/09/27 17:13:16 INFO Executor: Adding file:/tmp/spark-cfaf182b-71aa-4336-bff3-2abda40c348c/simple-project_2.10-1.0.jar to class loader
14/09/27 17:13:16 INFO BlockManager: Found block broadcast_0 locally
14/09/27 17:13:16 INFO CacheManager: Partition rdd_1_0 not found, computing it
14/09/27 17:13:16 INFO HadoopRDD: Input split: file:/usr/lib/spark/README.md:0+51
14/09/27 17:13:16 INFO MemoryStore: ensureFreeSpace(384) called with curMem=152694, maxMem=617427763
14/09/27 17:13:16 INFO MemoryStore: Block rdd_1_0 stored as values to memory (estimated size 384.0 B, free 588.7 MB)
14/09/27 17:13:16 INFO BlockManagerMasterActor$BlockManagerInfo: Added rdd_1_0 in memory on 192.168.171.1:55921 (size: 384.0 B, free: 588.8 MB)
14/09/27 17:13:16 INFO BlockManagerMaster: Updated info of block rdd_1_0
14/09/27 17:13:16 INFO Executor: Serialized size of result for 0 is 563
14/09/27 17:13:16 INFO Executor: Sending result for 0 directly to driver
14/09/27 17:13:16 INFO Executor: Finished task ID 0
14/09/27 17:13:16 INFO TaskSetManager: Starting task 0.0:1 as TID 1 on executor localhost: localhost (PROCESS_LOCAL)
14/09/27 17:13:16 INFO TaskSetManager: Serialized task 0.0:1 as 1690 bytes in 0 ms
14/09/27 17:13:16 INFO Executor: Running task ID 1
14/09/27 17:13:16 INFO BlockManager: Found block broadcast_0 locally
14/09/27 17:13:16 INFO DAGScheduler: Completed ResultTask(0, 0)
14/09/27 17:13:16 INFO CacheManager: Partition rdd_1_1 not found, computing it
14/09/27 17:13:16 INFO HadoopRDD: Input split: file:/usr/lib/spark/README.md:51+51
14/09/27 17:13:16 INFO TaskSetManager: Finished TID 0 in 318 ms on localhost (progress: 1/2)
14/09/27 17:13:16 INFO MemoryStore: ensureFreeSpace(544) called with curMem=153078, maxMem=617427763
14/09/27 17:13:16 INFO MemoryStore: Block rdd_1_1 stored as values to memory (estimated size 544.0 B, free 588.7 MB)
14/09/27 17:13:16 INFO BlockManagerMasterActor$BlockManagerInfo: Added rdd_1_1 in memory on 192.168.171.1:55921 (size: 544.0 B, free: 588.8 MB)
14/09/27 17:13:16 INFO BlockManagerMaster: Updated info of block rdd_1_1
14/09/27 17:13:16 INFO Executor: Serialized size of result for 1 is 563
14/09/27 17:13:16 INFO Executor: Sending result for 1 directly to driver
14/09/27 17:13:16 INFO Executor: Finished task ID 1
14/09/27 17:13:16 INFO TaskSetManager: Finished TID 1 in 21 ms on localhost (progress: 2/2)
14/09/27 17:13:16 INFO DAGScheduler: Completed ResultTask(0, 1)
14/09/27 17:13:16 INFO TaskSchedulerImpl: Removed TaskSet 0.0, whose tasks have all completed, from pool 
14/09/27 17:13:16 INFO DAGScheduler: Stage 0 (count at SimpleApp.scala:11) finished in 0.350 s
14/09/27 17:13:16 INFO SparkContext: Job finished: count at SimpleApp.scala:11, took 0.593880904 s
14/09/27 17:13:16 INFO SparkContext: Starting job: count at SimpleApp.scala:12
14/09/27 17:13:16 INFO DAGScheduler: Got job 1 (count at SimpleApp.scala:12) with 2 output partitions (allowLocal=false)
14/09/27 17:13:16 INFO DAGScheduler: Final stage: Stage 1 (count at SimpleApp.scala:12)
14/09/27 17:13:16 INFO DAGScheduler: Parents of final stage: List()
14/09/27 17:13:16 INFO DAGScheduler: Missing parents: List()
14/09/27 17:13:16 INFO DAGScheduler: Submitting Stage 1 (FilteredRDD[3] at filter at SimpleApp.scala:12), which has no missing parents
14/09/27 17:13:16 INFO DAGScheduler: Submitting 2 missing tasks from Stage 1 (FilteredRDD[3] at filter at SimpleApp.scala:12)
14/09/27 17:13:16 INFO TaskSchedulerImpl: Adding task set 1.0 with 2 tasks
14/09/27 17:13:16 INFO TaskSetManager: Starting task 1.0:0 as TID 2 on executor localhost: localhost (PROCESS_LOCAL)
14/09/27 17:13:16 INFO TaskSetManager: Serialized task 1.0:0 as 1693 bytes in 0 ms
14/09/27 17:13:16 INFO Executor: Running task ID 2
14/09/27 17:13:16 INFO BlockManager: Found block broadcast_0 locally
14/09/27 17:13:16 INFO BlockManager: Found block rdd_1_0 locally
14/09/27 17:13:16 INFO Executor: Serialized size of result for 2 is 563
14/09/27 17:13:16 INFO Executor: Sending result for 2 directly to driver
14/09/27 17:13:16 INFO Executor: Finished task ID 2
14/09/27 17:13:16 INFO TaskSetManager: Starting task 1.0:1 as TID 3 on executor localhost: localhost (PROCESS_LOCAL)
14/09/27 17:13:16 INFO TaskSetManager: Serialized task 1.0:1 as 1693 bytes in 0 ms
14/09/27 17:13:16 INFO Executor: Running task ID 3
14/09/27 17:13:16 INFO DAGScheduler: Completed ResultTask(1, 0)
14/09/27 17:13:16 INFO TaskSetManager: Finished TID 2 in 15 ms on localhost (progress: 1/2)
14/09/27 17:13:16 INFO BlockManager: Found block broadcast_0 locally
14/09/27 17:13:16 INFO BlockManager: Found block rdd_1_1 locally
14/09/27 17:13:16 INFO Executor: Serialized size of result for 3 is 563
14/09/27 17:13:16 INFO Executor: Sending result for 3 directly to driver
14/09/27 17:13:16 INFO Executor: Finished task ID 3
14/09/27 17:13:16 INFO TaskSetManager: Finished TID 3 in 13 ms on localhost (progress: 2/2)
14/09/27 17:13:16 INFO TaskSchedulerImpl: Removed TaskSet 1.0, whose tasks have all completed, from pool 
14/09/27 17:13:16 INFO DAGScheduler: Completed ResultTask(1, 1)
14/09/27 17:13:16 INFO DAGScheduler: Stage 1 (count at SimpleApp.scala:12) finished in 0.027 s
14/09/27 17:13:16 INFO SparkContext: Job finished: count at SimpleApp.scala:12, took 0.042803809 s
Lines with a: 8, Lines with b: 5
14/09/27 17:13:17 INFO MapOutputTrackerMasterActor: MapOutputTrackerActor stopped!
14/09/27 17:13:17 INFO ConnectionManager: Selector thread was interrupted!
14/09/27 17:13:18 INFO ConnectionManager: ConnectionManager stopped
14/09/27 17:13:18 INFO MemoryStore: MemoryStore cleared
14/09/27 17:13:18 INFO BlockManager: BlockManager stopped
14/09/27 17:13:18 INFO BlockManagerMasterActor: Stopping BlockManagerMaster
14/09/27 17:13:18 INFO BlockManagerMaster: BlockManagerMaster stopped
14/09/27 17:13:18 INFO SparkContext: Successfully stopped SparkContext
14/09/27 17:13:18 INFO RemoteActorRefProvider$RemotingTerminator: Shutting down remote daemon.
14/09/27 17:13:18 INFO RemoteActorRefProvider$RemotingTerminator: Remote daemon shut down; proceeding with flushing remote transports.
[success] Total time: 8 s, completed Sep 27, 2014 5:13:18 PM



comment out program 1, program 2 tests spark streaming. I know put into fns... going to delete this. has no value. my notes only

 System.setProperty("twitter4j.oauth.consumerKey", "eFIaiOuxsny01VVQ2QWISK1Mw")
    System.setProperty("twitter4j.oauth.consumerSecret", "gDQI5EiCMJJaaNI8XVNhfZXwuCOYfeJ3XsOUNHvsXqgq0Hoj9T")
    System.setProperty("twitter4j.oauth.accessToken", "76976448-Otz8w4yMKx6yCEWTH3dNTfuF8LYeLgqdoDrcl0oBK")
    System.setProperty("twitter4j.oauth.accessTokenSecret", "NFPFe2EzuKWuzRKmY1RENUBfQzGeGbAS1JzjX3Eu3GwDE")
       //scaladocs not accurate, follow holden's exampple
       //spark://192.168.171.1:7077
     val stream = new StreamingContext("local","Simple App", Seconds(1))
     val tweets= TwitterUtils.createStream(stream,None)
     tweets.print()
     stream.start()
     println("+++++++++++++++++++++++++++++");
     stream.awaitTermination()
    //sc.stop()



[dc@localhost TestSparkSBT]$ sbt/bin/sbt 
[info] Set current project to Simple Project (in build file:/home/dc/TestSpark/TestSparkSBT/)
> package
[info] Updating {file:/home/dc/TestSpark/TestSparkSBT/}testsparksbt...
[info] Resolving org.spark-project.akka#akka-remote_2.10;2.2.3-shaded-protobuf .[info] Resolving org.spark-project.akka#akka-actor_2.10;2.2.3-shaded-protobuf ..[info] Resolving org.spark-project.akka#akka-slf4j_2.10;2.2.3-shaded-protobuf ..[info] Resolving org.fusesource.jansi#jansi;1.4 ...
[info] Done updating.
[info] Compiling 3 Scala sources to /home/dc/TestSpark/TestSparkSBT/target/scala-2.10/classes...
[info] Packaging /home/dc/TestSpark/TestSparkSBT/target/scala-2.10/simple-project_2.10-1.0.jar ...
[info] Done packaging.
[success] Total time: 16 s, completed Sep 27, 2014 5:35:38 PM
> run
[info] Running SimpleApp 
14/09/27 17:35:42 INFO Utils: Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
14/09/27 17:35:42 WARN Utils: Your hostname, localhost.localdomain resolves to a loopback address: 127.0.0.1; using 192.168.171.1 instead (on interface vmnet8)
14/09/27 17:35:42 WARN Utils: Set SPARK_LOCAL_IP if you need to bind to another address
14/09/27 17:35:43 INFO Slf4jLogger: Slf4jLogger started
14/09/27 17:35:43 INFO Remoting: Starting remoting
14/09/27 17:35:43 INFO Remoting: Remoting started; listening on addresses :[akka.tcp://spark@192.168.171.1:47684]
14/09/27 17:35:43 INFO Remoting: Remoting now listens on addresses: [akka.tcp://spark@192.168.171.1:47684]
14/09/27 17:35:43 INFO SparkEnv: Registering BlockManagerMaster
14/09/27 17:35:43 INFO DiskBlockManager: Created local directory at /tmp/spark-local-20140927173543-8689
14/09/27 17:35:43 INFO MemoryStore: MemoryStore started with capacity 562.1 MB.
14/09/27 17:35:43 INFO ConnectionManager: Bound socket to port 39681 with id = ConnectionManagerId(192.168.171.1,39681)
14/09/27 17:35:43 INFO BlockManagerMaster: Trying to register BlockManager
14/09/27 17:35:43 INFO BlockManagerMasterActor$BlockManagerInfo: Registering block manager 192.168.171.1:39681 with 562.1 MB RAM
14/09/27 17:35:43 INFO BlockManagerMaster: Registered BlockManager
14/09/27 17:35:43 INFO HttpServer: Starting HTTP Server
14/09/27 17:35:44 INFO HttpBroadcast: Broadcast server started at http://192.168.171.1:57469
14/09/27 17:35:44 INFO SparkEnv: Registering MapOutputTracker
14/09/27 17:35:44 INFO HttpFileServer: HTTP File server directory is /tmp/spark-3038323f-9928-4d05-90f6-1b6522c7540f
14/09/27 17:35:44 INFO HttpServer: Starting HTTP Server
14/09/27 17:35:44 INFO SparkUI: Started Spark Web UI at http://192.168.171.1:4040
14/09/27 17:35:44 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
14/09/27 17:35:45 INFO NetworkInputTracker: NetworkInputTracker started
14/09/27 17:35:45 INFO SparkContext: Starting job: runJob at NetworkInputTracker.scala:182
14/09/27 17:35:45 INFO DAGScheduler: Got job 0 (runJob at NetworkInputTracker.scala:182) with 1 output partitions (allowLocal=false)
14/09/27 17:35:45 INFO DAGScheduler: Final stage: Stage 0 (runJob at NetworkInputTracker.scala:182)
14/09/27 17:35:45 INFO DAGScheduler: Parents of final stage: List()
14/09/27 17:35:45 INFO DAGScheduler: Missing parents: List()
14/09/27 17:35:45 INFO DAGScheduler: Submitting Stage 0 (ParallelCollectionRDD[0] at makeRDD at NetworkInputTracker.scala:165), which has no missing parents
14/09/27 17:35:45 INFO DAGScheduler: Submitting 1 missing tasks from Stage 0 (ParallelCollectionRDD[0] at makeRDD at NetworkInputTracker.scala:165)
14/09/27 17:35:45 INFO TaskSchedulerImpl: Adding task set 0.0 with 1 tasks
14/09/27 17:35:45 INFO TaskSetManager: Starting task 0.0:0 as TID 0 on executor localhost: localhost (PROCESS_LOCAL)
14/09/27 17:35:45 INFO TaskSetManager: Serialized task 0.0:0 as 4320 bytes in 7 ms
14/09/27 17:35:45 INFO Executor: Running task ID 0
14/09/27 17:35:45 INFO TwitterReceiver: Attempting to register with tracker
14/09/27 17:35:45 INFO NetworkReceiver$BlockGenerator: Block pushing thread started
14/09/27 17:35:45 INFO NetworkReceiver$BlockGenerator: Data handler started
14/09/27 17:35:45 INFO NetworkInputTracker: Registered receiver for network stream 0 from akka://spark
14/09/27 17:35:45 INFO TwitterStreamImpl: Establishing connection.
14/09/27 17:35:45 INFO TwitterReceiver: Twitter receiver started
14/09/27 17:35:45 INFO Executor: Serialized size of result for 0 is 525
14/09/27 17:35:45 INFO Executor: Sending result for 0 directly to driver
14/09/27 17:35:45 INFO Executor: Finished task ID 0
14/09/27 17:35:45 INFO TaskSetManager: Finished TID 0 in 131 ms on localhost (progress: 1/1)
14/09/27 17:35:45 INFO TaskSchedulerImpl: Removed TaskSet 0.0, whose tasks have all completed, from pool 
14/09/27 17:35:45 INFO DAGScheduler: Completed ResultTask(0, 0)
14/09/27 17:35:45 INFO DAGScheduler: Stage 0 (runJob at NetworkInputTracker.scala:182) finished in 0.146 s
14/09/27 17:35:45 INFO SparkContext: Job finished: runJob at NetworkInputTracker.scala:182, took 0.260528851 s
14/09/27 17:35:46 INFO ForEachDStream: metadataCleanupDelay = 3600
14/09/27 17:35:46 INFO TwitterInputDStream: metadataCleanupDelay = 3600
14/09/27 17:35:46 INFO TwitterInputDStream: Slide time = 1000 ms
14/09/27 17:35:46 INFO TwitterInputDStream: Storage level = StorageLevel(false, false, false, 1)
14/09/27 17:35:46 INFO TwitterInputDStream: Checkpoint interval = null
14/09/27 17:35:46 INFO TwitterInputDStream: Remember duration = 1000 ms
14/09/27 17:35:46 INFO TwitterInputDStream: Initialized and validated TwitterInputDStream@7833e208
14/09/27 17:35:46 INFO ForEachDStream: Slide time = 1000 ms
14/09/27 17:35:46 INFO ForEachDStream: Storage level = StorageLevel(false, false, false, 1)
14/09/27 17:35:46 INFO ForEachDStream: Checkpoint interval = null
14/09/27 17:35:46 INFO ForEachDStream: Remember duration = 1000 ms
14/09/27 17:35:46 INFO ForEachDStream: Initialized and validated org.apache.spark.streaming.dstream.ForEachDStream@163cb8df
14/09/27 17:35:46 INFO JobGenerator: JobGenerator started at 1411864547000 ms
14/09/27 17:35:46 INFO JobScheduler: JobScheduler started
+++++++++++++++++++++++++++++
14/09/27 17:35:47 INFO NetworkInputTracker: Stream 0 received 0 blocks
14/09/27 17:35:47 INFO JobScheduler: Added jobs for time 1411864547000 ms
-------------------------------------------
Time: 1411864547000 ms
-------------------------------------------

14/09/27 17:35:47 INFO JobScheduler: Starting job streaming job 1411864547000 ms.0 from job set of time 1411864547000 ms
14/09/27 17:35:47 INFO JobScheduler: Finished job streaming job 1411864547000 ms.0 from job set of time 1411864547000 ms
14/09/27 17:35:47 INFO JobScheduler: Total delay: 0.034 s for time 1411864547000 ms (execution: 0.001 s)
14/09/27 17:35:48 INFO NetworkInputTracker: Stream 0 received 0 blocks
14/09/27 17:35:48 INFO JobScheduler: Added jobs for time 1411864548000 ms
-------------------------------------------
Time: 1411864548000 ms
-------------------------------------------

14/09/27 17:35:48 INFO JobScheduler: Starting job streaming job 1411864548000 ms.0 from job set of time 1411864548000 ms
14/09/27 17:35:48 INFO JobScheduler: Finished job streaming job 1411864548000 ms.0 from job set of time 1411864548000 ms
14/09/27 17:35:48 INFO JobScheduler: Total delay: 0.003 s for time 1411864548000 ms (execution: 0.000 s)
14/09/27 17:35:49 INFO NetworkInputTracker: Stream 0 received 0 blocks
14/09/27 17:35:49 INFO JobScheduler: Added jobs for time 1411864549000 ms
-------------------------------------------
Time: 1411864549000 ms
-------------------------------------------

14/09/27 17:35:49 INFO JobScheduler: Starting job streaming job 1411864549000 ms.0 from job set of time 1411864549000 ms
14/09/27 17:35:49 INFO JobScheduler: Finished job streaming job 1411864549000 ms.0 from job set of time 1411864549000 ms
14/09/27 17:35:49 INFO JobScheduler: Total delay: 0.002 s for time 1411864549000 ms (execution: 0.000 s)
14/09/27 17:35:50 INFO NetworkInputTracker: Stream 0 received 0 blocks
14/09/27 17:35:50 INFO JobScheduler: Added jobs for time 1411864550000 ms
-------------------------------------------
Time: 1411864550000 ms14/09/27 17:35:50 INFO JobScheduler: Starting job streaming job 1411864550000 ms.0 from job set of time 1411864550000 ms

-------------------------------------------

14/09/27 17:35:50 INFO JobScheduler: Finished job streaming job 1411864550000 ms.0 from job set of time 1411864550000 ms
14/09/27 17:35:50 INFO JobScheduler: Total delay: 0.002 s for time 1411864550000 ms (execution: 0.000 s)
14/09/27 17:35:51 INFO NetworkInputTracker: Stream 0 received 0 blocks
14/09/27 17:35:51 INFO JobScheduler: Added jobs for time 1411864551000 ms
-------------------------------------------
Time: 1411864551000 ms
-------------------------------------------
14/09/27 17:35:51 INFO JobScheduler: Starting job streaming job 1411864551000 ms.0 from job set of time 1411864551000 ms

14/09/27 17:35:51 INFO JobScheduler: Finished job streaming job 1411864551000 ms.0 from job set of time 1411864551000 ms
14/09/27 17:35:51 INFO JobScheduler: Total delay: 0.002 s for time 1411864551000 ms (execution: 0.000 s)


program 3 test b/w of spark

