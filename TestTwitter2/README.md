org.apache.spark.SparkConf@55afc1de
14/09/27 14:09:20 WARN util.Utils: Your hostname, localhost.localdomain resolves to a loopback address: 127.0.0.1; using 192.168.171.1 instead (on interface vmnet8)
14/09/27 14:09:20 WARN util.Utils: Set SPARK_LOCAL_IP if you need to bind to another address
14/09/27 14:09:20 INFO spark.SecurityManager: Changing view acls to: dc
14/09/27 14:09:20 INFO spark.SecurityManager: SecurityManager: authentication disabled; ui acls disabled; users with view permissions: Set(dc)
14/09/27 14:09:21 INFO slf4j.Slf4jLogger: Slf4jLogger started
14/09/27 14:09:21 INFO Remoting: Starting remoting
14/09/27 14:09:21 INFO Remoting: Remoting started; listening on addresses :[akka.tcp://spark@192.168.171.1:34399]
14/09/27 14:09:21 INFO Remoting: Remoting now listens on addresses: [akka.tcp://spark@192.168.171.1:34399]
14/09/27 14:09:21 INFO spark.SparkEnv: Registering MapOutputTracker
14/09/27 14:09:21 INFO spark.SparkEnv: Registering BlockManagerMaster
14/09/27 14:09:21 INFO storage.DiskBlockManager: Created local directory at /tmp/spark-local-20140927140921-2dca
14/09/27 14:09:21 INFO storage.MemoryStore: MemoryStore started with capacity 1023.0 MB.
14/09/27 14:09:21 INFO network.ConnectionManager: Bound socket to port 45202 with id = ConnectionManagerId(192.168.171.1,45202)
14/09/27 14:09:21 INFO storage.BlockManagerMaster: Trying to register BlockManager
14/09/27 14:09:21 INFO storage.BlockManagerInfo: Registering block manager 192.168.171.1:45202 with 1023.0 MB RAM
14/09/27 14:09:21 INFO storage.BlockManagerMaster: Registered BlockManager
14/09/27 14:09:21 INFO spark.HttpServer: Starting HTTP Server
14/09/27 14:09:22 INFO server.Server: jetty-8.1.14.v20131031
14/09/27 14:09:22 INFO server.AbstractConnector: Started SocketConnector@0.0.0.0:45312
14/09/27 14:09:22 INFO broadcast.HttpBroadcast: Broadcast server started at http://192.168.171.1:45312
14/09/27 14:09:22 INFO spark.HttpFileServer: HTTP File server directory is /tmp/spark-1651d6c7-4122-4276-b2fe-930847551593
14/09/27 14:09:22 INFO spark.HttpServer: Starting HTTP Server
14/09/27 14:09:22 INFO server.Server: jetty-8.1.14.v20131031
14/09/27 14:09:22 INFO server.AbstractConnector: Started SocketConnector@0.0.0.0:38594
14/09/27 14:09:22 INFO server.Server: jetty-8.1.14.v20131031
14/09/27 14:09:22 INFO server.AbstractConnector: Started SelectChannelConnector@0.0.0.0:4040
14/09/27 14:09:22 INFO ui.SparkUI: Started SparkUI at http://192.168.171.1:4040
14/09/27 14:09:23 INFO scheduler.ReceiverTracker: ReceiverTracker started
14/09/27 14:09:23 INFO dstream.ForEachDStream: metadataCleanupDelay = -1
14/09/27 14:09:23 INFO twitter.TwitterInputDStream: metadataCleanupDelay = -1
14/09/27 14:09:23 INFO twitter.TwitterInputDStream: Slide time = 1000 ms
14/09/27 14:09:23 INFO twitter.TwitterInputDStream: Storage level = StorageLevel(false, false, false, false, 1)
14/09/27 14:09:23 INFO twitter.TwitterInputDStream: Checkpoint interval = null
14/09/27 14:09:23 INFO twitter.TwitterInputDStream: Remember duration = 1000 ms
14/09/27 14:09:23 INFO twitter.TwitterInputDStream: Initialized and validated org.apache.spark.streaming.twitter.TwitterInputDStream@329556e2
14/09/27 14:09:23 INFO dstream.ForEachDStream: Slide time = 1000 ms
14/09/27 14:09:23 INFO dstream.ForEachDStream: Storage level = StorageLevel(false, false, false, false, 1)
14/09/27 14:09:23 INFO dstream.ForEachDStream: Checkpoint interval = null
14/09/27 14:09:23 INFO dstream.ForEachDStream: Remember duration = 1000 ms
14/09/27 14:09:23 INFO dstream.ForEachDStream: Initialized and validated org.apache.spark.streaming.dstream.ForEachDStream@72133137
14/09/27 14:09:23 INFO scheduler.ReceiverTracker: Starting 1 receivers
14/09/27 14:09:23 INFO spark.SparkContext: Starting job: runJob at ReceiverTracker.scala:275
14/09/27 14:09:23 INFO scheduler.DAGScheduler: Got job 0 (runJob at ReceiverTracker.scala:275) with 1 output partitions (allowLocal=false)
14/09/27 14:09:23 INFO scheduler.DAGScheduler: Final stage: Stage 0(runJob at ReceiverTracker.scala:275)
14/09/27 14:09:23 INFO scheduler.DAGScheduler: Parents of final stage: List()
14/09/27 14:09:23 INFO scheduler.DAGScheduler: Missing parents: List()
14/09/27 14:09:23 INFO scheduler.DAGScheduler: Submitting Stage 0 (ParallelCollectionRDD[0] at makeRDD at ReceiverTracker.scala:253), which has no missing parents
14/09/27 14:09:23 INFO util.RecurringTimer: Started timer for JobGenerator at time 1411852164000
14/09/27 14:09:23 INFO scheduler.JobGenerator: Started JobGenerator at 1411852164000 ms
14/09/27 14:09:23 INFO scheduler.JobScheduler: Started JobScheduler
+++++++++++++++++++++++++++++
14/09/27 14:09:23 INFO scheduler.DAGScheduler: Submitting 1 missing tasks from Stage 0 (ParallelCollectionRDD[0] at makeRDD at ReceiverTracker.scala:253)
14/09/27 14:09:23 INFO scheduler.TaskSchedulerImpl: Adding task set 0.0 with 1 tasks
14/09/27 14:09:23 INFO scheduler.TaskSetManager: Starting task 0.0:0 as TID 0 on executor localhost: localhost (PROCESS_LOCAL)
14/09/27 14:09:23 INFO scheduler.TaskSetManager: Serialized task 0.0:0 as 4145 bytes in 4 ms
14/09/27 14:09:23 INFO executor.Executor: Running task ID 0
14/09/27 14:09:23 INFO receiver.ReceiverSupervisorImpl: Registered receiver 0
14/09/27 14:09:23 INFO util.RecurringTimer: Started timer for BlockGenerator at time 1411852163800
14/09/27 14:09:23 INFO receiver.BlockGenerator: Started BlockGenerator
14/09/27 14:09:23 INFO receiver.BlockGenerator: Started block pushing thread
14/09/27 14:09:23 INFO receiver.ReceiverSupervisorImpl: Starting receiver
14/09/27 14:09:23 INFO scheduler.ReceiverTracker: Registered receiver for stream 0 from akka://spark
14/09/27 14:09:23 INFO twitter4j.TwitterStreamImpl: Establishing connection.
14/09/27 14:09:23 INFO twitter.TwitterReceiver: Twitter receiver started
14/09/27 14:09:23 INFO receiver.ReceiverSupervisorImpl: Called receiver onStart
14/09/27 14:09:23 INFO scheduler.ReceiverTracker: Registered receiver for stream 0 from akka://spark
14/09/27 14:09:24 INFO scheduler.ReceiverTracker: Stream 0 received 0 blocks
14/09/27 14:09:24 INFO scheduler.JobScheduler: Added jobs for time 1411852164000 ms
-------------------------------------------
Time: 1411852164000 ms
-------------------------------------------
14/09/27 14:09:24 INFO scheduler.JobScheduler: Starting job streaming job 1411852164000 ms.0 from job set of time 1411852164000 ms

14/09/27 14:09:24 INFO scheduler.JobScheduler: Finished job streaming job 1411852164000 ms.0 from job set of time 1411852164000 ms
14/09/27 14:09:24 INFO scheduler.JobScheduler: Total delay: 0.052 s for time 1411852164000 ms (execution: 0.003 s)
14/09/27 14:09:24 INFO twitter4j.TwitterStreamImpl: Connection established.
14/09/27 14:09:24 INFO twitter4j.TwitterStreamImpl: Receiving status stream.
14/09/27 14:09:25 INFO scheduler.ReceiverTracker: Stream 0 received 0 blocks
14/09/27 14:09:25 INFO scheduler.JobScheduler: Added jobs for time 1411852165000 ms
-------------------------------------------
14/09/27 14:09:25 INFO scheduler.JobScheduler: Starting job streaming job 1411852165000 ms.0 from job set of time 1411852165000 ms
14/09/27 14:09:25 INFO scheduler.JobScheduler: Finished job streaming job 1411852165000 ms.0 from job set of time 1411852165000 ms
14/09/27 14:09:25 INFO scheduler.JobScheduler: Total delay: 0.005 s for time 1411852165000 ms (execution: 0.000 s)
Time: 1411852165000 ms
-------------------------------------------

14/09/27 14:09:25 INFO rdd.BlockRDD: Removing RDD 1 from persistence list
14/09/27 14:09:25 INFO storage.BlockManager: Removing RDD 1
14/09/27 14:09:25 INFO twitter.TwitterInputDStream: Removing blocks of RDD BlockRDD[1] at BlockRDD at ReceiverInputDStream.scala:69 of time 1411852165000 ms
14/09/27 14:09:25 INFO storage.MemoryStore: ensureFreeSpace(5902) called with curMem=0, maxMem=1072653926
14/09/27 14:09:25 INFO storage.MemoryStore: Block input-0-1411852164800 stored as bytes to memory (size 5.8 KB, free 1023.0 MB)
14/09/27 14:09:25 INFO storage.BlockManagerInfo: Added input-0-1411852164800 in memory on 192.168.171.1:45202 (size: 5.8 KB, free: 1023.0 MB)
14/09/27 14:09:25 INFO storage.BlockManagerMaster: Updated info of block input-0-1411852164800
14/09/27 14:09:25 INFO network.SendingConnection: Initiating connection to [/192.168.171.1:45202]
14/09/27 14:09:25 INFO network.ConnectionManager: Accepted connection from [192.168.171.1/192.168.171.1]
14/09/27 14:09:25 INFO network.SendingConnection: Connected to [/192.168.171.1:45202], 1 messages pending
14/09/27 14:09:25 WARN storage.BlockManager: Block input-0-1411852164800 already exists on this machine; not re-adding it
14/09/27 14:09:25 INFO receiver.BlockGenerator: Pushed block input-0-1411852164800
14/09/27 14:09:25 INFO storage.MemoryStore: ensureFreeSpace(51068) called with curMem=5902, maxMem=1072653926
14/09/27 14:09:25 INFO storage.MemoryStore: Block input-0-1411852165000 stored as bytes to memory (size 49.9 KB, free 1022.9 MB)
14/09/27 14:09:25 INFO storage.BlockManagerInfo: Added input-0-1411852165000 in memory on 192.168.171.1:45202 (size: 49.9 KB, free: 1022.9 MB)
14/09/27 14:09:25 INFO storage.BlockManagerMaster: Updated info of block input-0-1411852165000
14/09/27 14:09:25 WARN storage.BlockManager: Block input-0-1411852165000 already exists on this machine; not re-adding it
14/09/27 14:09:25 INFO receiver.BlockGenerator: Pushed block input-0-1411852165000
14/09/27 14:09:25 INFO storage.MemoryStore: ensureFreeSpace(8066) called with curMem=56970, maxMem=1072653926
14/09/27 14:09:25 INFO storage.MemoryStore: Block input-0-1411852165200 stored as bytes to memory (size 7.9 KB, free 1022.9 MB)
14/09/27 14:09:25 INFO storage.BlockManagerInfo: Added input-0-1411852165200 in memory on 192.168.171.1:45202 (size: 7.9 KB, free: 1022.9 MB)
14/09/27 14:09:25 INFO storage.BlockManagerMaster: Updated info of block input-0-1411852165200
14/09/27 14:09:25 WARN storage.BlockManager: Block input-0-1411852165200 already exists on this machine; not re-adding it
14/09/27 14:09:25 INFO receiver.BlockGenerator: Pushed block input-0-1411852165200
14/09/27 14:09:26 INFO scheduler.ReceiverTracker: Stream 0 received 3 blocks
14/09/27 14:09:26 INFO scheduler.JobScheduler: Added jobs for time 1411852166000 ms
14/09/27 14:09:26 INFO scheduler.JobScheduler: Starting job streaming job 1411852166000 ms.0 from job set of time 1411852166000 ms
14/09/27 14:09:26 INFO spark.SparkContext: Starting job: take at DStream.scala:593
14/09/27 14:09:26 INFO scheduler.DAGScheduler: Got job 1 (take at DStream.scala:593) with 1 output partitions (allowLocal=true)
14/09/27 14:09:26 INFO scheduler.DAGScheduler: Final stage: Stage 1(take at DStream.scala:593)
14/09/27 14:09:26 INFO scheduler.DAGScheduler: Parents of final stage: List()
14/09/27 14:09:26 INFO scheduler.DAGScheduler: Missing parents: List()
14/09/27 14:09:26 INFO scheduler.DAGScheduler: Computing the requested partition locally
14/09/27 14:09:26 INFO storage.BlockManager: Found block input-0-1411852164800 locally
14/09/27 14:09:26 INFO storage.MemoryStore: ensureFreeSpace(46331) called with curMem=65036, maxMem=1072653926
14/09/27 14:09:26 INFO storage.MemoryStore: Block input-0-1411852165800 stored as bytes to memory (size 45.2 KB, free 1022.9 MB)
14/09/27 14:09:26 INFO storage.BlockManagerInfo: Added input-0-1411852165800 in memory on 192.168.171.1:45202 (size: 45.2 KB, free: 1022.9 MB)
14/09/27 14:09:26 INFO storage.BlockManagerMaster: Updated info of block input-0-1411852165800
14/09/27 14:09:26 INFO spark.SparkContext: Job finished: take at DStream.scala:593, took 0.024329296 s
14/09/27 14:09:26 INFO spark.SparkContext: Starting job: take at DStream.scala:593
14/09/27 14:09:26 INFO scheduler.DAGScheduler: Got job 2 (take at DStream.scala:593) with 2 output partitions (allowLocal=true)
14/09/27 14:09:26 INFO scheduler.DAGScheduler: Final stage: Stage 2(take at DStream.scala:593)
14/09/27 14:09:26 INFO scheduler.DAGScheduler: Parents of final stage: List()
14/09/27 14:09:26 INFO scheduler.DAGScheduler: Missing parents: List()
14/09/27 14:09:26 INFO scheduler.DAGScheduler: Submitting Stage 2 (BlockRDD[3] at BlockRDD at ReceiverInputDStream.scala:69), which has no missing parents
14/09/27 14:09:26 INFO scheduler.DAGScheduler: Submitting 2 missing tasks from Stage 2 (BlockRDD[3] at BlockRDD at ReceiverInputDStream.scala:69)
14/09/27 14:09:26 INFO scheduler.TaskSchedulerImpl: Adding task set 2.0 with 2 tasks
14/09/27 14:09:26 WARN storage.BlockManager: Block input-0-1411852165800 already exists on this machine; not re-adding it
14/09/27 14:09:26 INFO receiver.BlockGenerator: Pushed block input-0-1411852165800
14/09/27 14:09:26 INFO storage.MemoryStore: ensureFreeSpace(18259) called with curMem=111367, maxMem=1072653926
14/09/27 14:09:26 INFO storage.MemoryStore: Block input-0-1411852166000 stored as bytes to memory (size 17.8 KB, free 1022.8 MB)
14/09/27 14:09:26 INFO storage.BlockManagerInfo: Added input-0-1411852166000 in memory on 192.168.171.1:45202 (size: 17.8 KB, free: 1022.8 MB)
14/09/27 14:09:26 INFO storage.BlockManagerMaster: Updated info of block input-0-1411852166000
14/09/27 14:09:26 WARN storage.BlockManager: Block input-0-1411852166000 already exists on this machine; not re-adding it
14/09/27 14:09:26 INFO receiver.BlockGenerator: Pushed block input-0-1411852166000
14/09/27 14:09:26 INFO storage.MemoryStore: ensureFreeSpace(3585) called with curMem=129626, maxMem=1072653926
14/09/27 14:09:26 INFO storage.MemoryStore: Block input-0-1411852166400 stored as bytes to memory (size 3.5 KB, free 1022.8 MB)
14/09/27 14:09:26 INFO storage.BlockManagerInfo: Added input-0-1411852166400 in memory on 192.168.171.1:45202 (size: 3.5 KB, free: 1022.8 MB)
14/09/27 14:09:26 INFO storage.BlockManagerMaster: Updated info of block input-0-1411852166400
14/09/27 14:09:26 WARN storage.BlockManager: Block input-0-1411852166400 already exists on this machine; not re-adding it
14/09/27 14:09:26 INFO receiver.BlockGenerator: Pushed block input-0-1411852166400
14/09/27 14:09:27 INFO scheduler.ReceiverTracker: Stream 0 received 3 blocks
14/09/27 14:09:27 INFO scheduler.JobScheduler: Added jobs for time 1411852167000 ms
14/09/27 14:09:27 INFO storage.MemoryStore: ensureFreeSpace(43547) called with curMem=133211, maxMem=1072653926
14/09/27 14:09:27 INFO storage.MemoryStore: Block input-0-1411852166800 stored as bytes to memory (size 42.5 KB, free 1022.8 MB)
14/09/27 14:09:27 INFO storage.BlockManagerInfo: Added input-0-1411852166800 in memory on 192.168.171.1:45202 (size: 42.5 KB, free: 1022.8 MB)
14/09/27 14:09:27 INFO storage.BlockManagerMaster: Updated info of block input-0-1411852166800
14/09/27 14:09:27 WARN storage.BlockManager: Block input-0-1411852166800 already exists on this machine; not re-adding it
14/09/27 14:09:27 INFO receiver.BlockGenerator: Pushed block input-0-1411852166800
14/09/27 14:09:27 INFO storage.MemoryStore: ensureFreeSpace(30104) called with curMem=176758, maxMem=1072653926
14/09/27 14:09:27 INFO storage.MemoryStore: Block input-0-1411852167000 stored as bytes to memory (size 29.4 KB, free 1022.8 MB)
14/09/27 14:09:27 INFO storage.BlockManagerInfo: Added input-0-1411852167000 in memory on 192.168.171.1:45202 (size: 29.4 KB, free: 1022.8 MB)
14/09/27 14:09:27 INFO storage.BlockManagerMaster: Updated info of block input-0-1411852167000
14/09/27 14:09:27 WARN storage.BlockManager: Block input-0-1411852167000 already exists on this machine; not re-adding it
14/09/27 14:09:27 INFO receiver.BlockGenerator: Pushed block input-0-1411852167000
14/09/27 14:09:28 INFO scheduler.ReceiverTracker: Stream 0 received 2 blocks
14/09/27 14:09:28 INFO scheduler.JobScheduler: Added jobs for time 1411852168000 ms
14/09/27 14:09:28 INFO storage.MemoryStore: ensureFreeSpace(55357) called with curMem=206862, maxMem=1072653926
14/09/27 14:09:28 INFO storage.MemoryStore: Block input-0-1411852167800 stored as bytes to memory (size 54.1 KB, free 1022.7 MB)
14/09/27 14:09:28 INFO storage.BlockManagerInfo: Added input-0-1411852167800 in memory on 192.168.171.1:45202 (size: 54.1 KB, free: 1022.7 MB)
14/09/27 14:09:28 INFO storage.BlockManagerMaster: Updated info of block input-0-1411852167800
14/09/27 14:09:28 WARN storage.BlockManager: Block input-0-1411852167800 already exists on this machine; not re-adding it
14/09/27 14:09:28 INFO receiver.BlockGenerator: Pushed block input-0-1411852167800
14/09/27 14:09:28 INFO storage.MemoryStore: ensureFreeSpace(18664) called with curMem=262219, maxMem=1072653926
14/09/27 14:09:28 INFO storage.MemoryStore: Block input-0-1411852168000 stored as bytes to memory (size 18.2 KB, free 1022.7 MB)
14/09/27 14:09:28 INFO storage.BlockManagerInfo: Added input-0-1411852168000 in memory on 192.168.171.1:45202 (size: 18.2 KB, free: 1022.7 MB)
14/09/27 14:09:28 INFO storage.BlockManagerMaster: Updated info of block input-0-1411852168000
14/09/27 14:09:28 WARN storage.BlockManager: Block input-0-1411852168000 already exists on this machine; not re-adding it
14/09/27 14:09:28 INFO receiver.BlockGenerator: Pushed block input-0-1411852168000
14/09/27 14:09:29 INFO scheduler.ReceiverTracker: Stream 0 received 2 blocks
14/09/27 14:09:29 INFO scheduler.JobScheduler: Added jobs for time 1411852169000 ms
14/09/27 14:09:29 INFO storage.MemoryStore: ensureFreeSpace(60279) called with curMem=280883, maxMem=1072653926
14/09/27 14:09:29 INFO storage.MemoryStore: Block input-0-1411852168800 stored as bytes to memory (size 58.9 KB, free 1022.6 MB)
14/09/27 14:09:29 INFO storage.BlockManagerInfo: Added input-0-1411852168800 in memory on 192.168.171.1:45202 (size: 58.9 KB, free: 1022.6 MB)
14/09/27 14:09:29 INFO storage.BlockManagerMaster: Updated info of block input-0-1411852168800
14/09/27 14:09:29 WARN storage.BlockManager: Block input-0-1411852168800 already exists on this machine; not re-adding it
14/09/27 14:09:29 INFO receiver.BlockGenerator: Pushed block input-0-1411852168800
14/09/27 14:09:29 INFO storage.MemoryStore: ensureFreeSpace(10776) called with curMem=341162, maxMem=1072653926
14/09/27 14:09:29 INFO storage.MemoryStore: Block input-0-1411852169000 stored as bytes to memory (size 10.5 KB, free 1022.6 MB)
14/09/27 14:09:29 INFO storage.BlockManagerInfo: Added input-0-1411852169000 in memory on 192.168.171.1:45202 (size: 10.5 KB, free: 1022.6 MB)
14/09/27 14:09:29 INFO storage.BlockManagerMaster: Updated info of block input-0-1411852169000
14/09/27 14:09:29 WARN storage.BlockManager: Block input-0-1411852169000 already exists on this machine; not re-adding it
14/09/27 14:09:29 INFO receiver.BlockGenerator: Pushed block input-0-1411852169000
14/09/27 14:09:29 INFO storage.MemoryStore: ensureFreeSpace(3453) called with curMem=351938, maxMem=1072653926
14/09/27 14:09:29 INFO storage.MemoryStore: Block input-0-1411852169200 stored as bytes to memory (size 3.4 KB, free 1022.6 MB)
14/09/27 14:09:29 INFO storage.BlockManagerInfo: Added input-0-1411852169200 in memory on 192.168.171.1:45202 (size: 3.4 KB, free: 1022.6 MB)
14/09/27 14:09:29 INFO storage.BlockManagerMaster: Updated info of block input-0-1411852169200
14/09/27 14:09:29 WARN storage.BlockManager: Block input-0-1411852169200 already exists on this machine; not re-adding it
14/09/27 14:09:29 INFO receiver.BlockGenerator: Pushed block input-0-1411852169200
14/09/27 14:09:30 INFO scheduler.ReceiverTracker: Stream 0 received 3 blocks
14/09/27 14:09:30 INFO scheduler.JobScheduler: Added jobs for time 1411852170000 ms
14/09/27 14:09:30 INFO storage.MemoryStore: ensureFreeSpace(39517) called with curMem=355391, maxMem=1072653926
14/09/27 14:09:30 INFO storage.MemoryStore: Block input-0-1411852169800 stored as bytes to memory (size 38.6 KB, free 1022.6 MB)
14/09/27 14:09:30 INFO storage.BlockManagerInfo: Added input-0-1411852169800 in memory on 192.168.171.1:45202 (size: 38.6 KB, free: 1022.6 MB)
14/09/27 14:09:30 INFO storage.BlockManagerMaster: Updated info of block input-0-1411852169800
14/09/27 14:09:30 WARN storage.BlockManager: Block input-0-1411852169800 already exists on this machine; not re-adding it
14/09/27 14:09:30 INFO receiver.BlockGenerator: Pushed block input-0-1411852169800
14/09/27 14:09:30 INFO storage.MemoryStore: ensureFreeSpace(22431) called with curMem=394908, maxMem=1072653926
14/09/27 14:09:30 INFO storage.MemoryStore: Block input-0-1411852170000 stored as bytes to memory (size 21.9 KB, free 1022.6 MB)
14/09/27 14:09:30 INFO storage.BlockManagerInfo: Added input-0-1411852170000 in memory on 192.168.171.1:45202 (size: 21.9 KB, free: 1022.6 MB)
14/09/27 14:09:30 INFO storage.BlockManagerMaster: Updated info of block input-0-1411852170000
14/09/27 14:09:30 WARN storage.BlockManager: Block input-0-1411852170000 already exists on this machine; not re-adding it
14/09/27 14:09:30 INFO receiver.BlockGenerator: Pushed block input-0-1411852170000
14/09/27 14:09:30 INFO storage.MemoryStore: ensureFreeSpace(2823) called with curMem=417339, maxMem=1072653926
14/09/27 14:09:30 INFO storage.MemoryStore: Block input-0-1411852170200 stored as bytes to memory (size 2.8 KB, free 1022.6 MB)
14/09/27 14:09:30 INFO storage.BlockManagerInfo: Added input-0-1411852170200 in memory on 192.168.171.1:45202 (size: 2.8 KB, free: 1022.6 MB)
14/09/27 14:09:30 INFO storage.BlockManagerMaster: Updated info of block input-0-1411852170200
14/09/27 14:09:30 WARN storage.BlockManager: Block input-0-1411852170200 already exists on this machine; not re-adding it
14/09/27 14:09:30 INFO receiver.BlockGenerator: Pushed block input-0-1411852170200
14/09/27 14:09:31 INFO scheduler.ReceiverTracker: Stream 0 received 3 blocks
14/09/27 14:09:31 INFO scheduler.JobScheduler: Added jobs for time 1411852171000 ms
14/09/27 14:09:31 INFO storage.MemoryStore: ensureFreeSpace(64091) called with curMem=420162, maxMem=1072653926
14/09/27 14:09:31 INFO storage.MemoryStore: Block input-0-1411852170800 stored as bytes to memory (size 62.6 KB, free 1022.5 MB)
14/09/27 14:09:31 INFO storage.BlockManagerInfo: Added input-0-1411852170800 in memory on 192.168.171.1:45202 (size: 62.6 KB, free: 1022.5 MB)
14/09/27 14:09:31 INFO storage.BlockManagerMaster: Updated info of block input-0-1411852170800
14/09/27 14:09:31 WARN storage.BlockManager: Block input-0-1411852170800 already exists on this machine; not re-adding it
14/09/27 14:09:31 INFO receiver.BlockGenerator: Pushed block input-0-1411852170800
14/09/27 14:09:31 INFO storage.MemoryStore: ensureFreeSpace(22850) called with curMem=484253, maxMem=1072653926
14/09/27 14:09:31 INFO storage.MemoryStore: Block input-0-1411852171000 stored as bytes to memory (size 22.3 KB, free 1022.5 MB)
14/09/27 14:09:31 INFO storage.BlockManagerInfo: Added input-0-1411852171000 in memory on 192.168.171.1:45202 (size: 22.3 KB, free: 1022.5 MB)
14/09/27 14:09:31 INFO storage.BlockManagerMaster: Updated info of block input-0-1411852171000
14/09/27 14:09:31 WARN storage.BlockManager: Block input-0-1411852171000 already exists on this machine; not re-adding it
14/09/27 14:09:31 INFO receiver.BlockGenerator: Pushed block input-0-1411852171000
14/09/27 14:09:32 INFO scheduler.ReceiverTracker: Stream 0 received 2 blocks
14/09/27 14:09:32 INFO scheduler.JobScheduler: Added jobs for time 1411852172000 ms
14/09/27 14:09:32 INFO storage.MemoryStore: ensureFreeSpace(47498) called with curMem=507103, maxMem=1072653926
14/09/27 14:09:32 INFO storage.MemoryStore: Block input-0-1411852171800 stored as bytes to memory (size 46.4 KB, free 1022.4 MB)
14/09/27 14:09:32 INFO storage.BlockManagerInfo: Added input-0-1411852171800 in memory on 192.168.171.1:45202 (size: 46.4 KB, free: 1022.4 MB)
14/09/27 14:09:32 INFO storage.BlockManagerMaster: Updated info of block input-0-1411852171800
14/09/27 14:09:32 WARN storage.BlockManager: Block input-0-1411852171800 already exists on this machine; not re-adding it
14/09/27 14:09:32 INFO receiver.BlockGenerator: Pushed block input-0-1411852171800
14/09/27 14:09:32 INFO storage.MemoryStore: ensureFreeSpace(18842) called with curMem=554601, maxMem=1072653926
14/09/27 14:09:32 INFO storage.MemoryStore: Block input-0-1411852172000 stored as bytes to memory (size 18.4 KB, free 1022.4 MB)
14/09/27 14:09:32 INFO storage.BlockManagerInfo: Added input-0-1411852172000 in memory on 192.168.171.1:45202 (size: 18.4 KB, free: 1022.4 MB)
14/09/27 14:09:32 INFO storage.BlockManagerMaster: Updated info of block input-0-1411852172000
14/09/27 14:09:32 WARN storage.BlockManager: Block input-0-1411852172000 already exists on this machine; not re-adding it
14/09/27 14:09:32 INFO receiver.BlockGenerator: Pushed block input-0-1411852172000
14/09/27 14:09:32 INFO storage.MemoryStore: ensureFreeSpace(7086) called with curMem=573443, maxMem=1072653926
14/09/27 14:09:32 INFO storage.MemoryStore: Block input-0-1411852172200 stored as bytes to memory (size 6.9 KB, free 1022.4 MB)
14/09/27 14:09:32 INFO storage.BlockManagerInfo: Added input-0-1411852172200 in memory on 192.168.171.1:45202 (size: 6.9 KB, free: 1022.4 MB)
14/09/27 14:09:32 INFO storage.BlockManagerMaster: Updated info of block input-0-1411852172200
14/09/27 14:09:32 WARN storage.BlockManager: Block input-0-1411852172200 already exists on this machine; not re-adding it
14/09/27 14:09:32 INFO receiver.BlockGenerator: Pushed block input-0-1411852172200
14/09/27 14:09:33 INFO scheduler.ReceiverTracker: Stream 0 received 3 blocks
14/09/27 14:09:33 INFO scheduler.JobScheduler: Added jobs for time 1411852173000 ms
14/09/27 14:09:33 INFO storage.MemoryStore: ensureFreeSpace(46021) called with curMem=580529, maxMem=1072653926
14/09/27 14:09:33 INFO storage.MemoryStore: Block input-0-1411852172800 stored as bytes to memory (size 44.9 KB, free 1022.4 MB)
14/09/27 14:09:33 INFO storage.BlockManagerInfo: Added input-0-1411852172800 in memory on 192.168.171.1:45202 (size: 44.9 KB, free: 1022.4 MB)
14/09/27 14:09:33 INFO storage.BlockManagerMaster: Updated info of block input-0-1411852172800
14/09/27 14:09:33 WARN storage.BlockManager: Block input-0-1411852172800 already exists on this machine; not re-adding it
14/09/27 14:09:33 INFO receiver.BlockGenerator: Pushed block input-0-1411852172800
14/09/27 14:09:33 INFO storage.MemoryStore: ensureFreeSpace(17693) called with curMem=626550, maxMem=1072653926
14/09/27 14:09:33 INFO storage.MemoryStore: Block input-0-1411852173000 stored as bytes to memory (size 17.3 KB, free 1022.3 MB)
14/09/27 14:09:33 INFO storage.BlockManagerInfo: Added input-0-1411852173000 in memory on 192.168.171.1:45202 (size: 17.3 KB, free: 1022.3 MB)
14/09/27 14:09:33 INFO storage.BlockManagerMaster: Updated info of block input-0-1411852173000
14/09/27 14:09:33 WARN storage.BlockManager: Block input-0-1411852173000 already exists on this machine; not re-adding it
14/09/27 14:09:33 INFO receiver.BlockGenerator: Pushed block input-0-1411852173000
14/09/27 14:09:33 INFO storage.MemoryStore: ensureFreeSpace(3340) called with curMem=644243, maxMem=1072653926
14/09/27 14:09:33 INFO storage.MemoryStore: Block input-0-1411852173200 stored as bytes to memory (size 3.3 KB, free 1022.3 MB)
14/09/27 14:09:33 INFO storage.BlockManagerInfo: Added input-0-1411852173200 in memory on 192.168.171.1:45202 (size: 3.3 KB, free: 1022.3 MB)
14/09/27 14:09:33 INFO storage.BlockManagerMaster: Updated info of block input-0-1411852173200
14/09/27 14:09:33 WARN storage.BlockManager: Block input-0-1411852173200 already exists on this machine; not re-adding it
14/09/27 14:09:33 INFO receiver.BlockGenerator: Pushed block input-0-1411852173200

