/*** SimpleApp.scala ***/
import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.streaming._

object SimpleApp {
  def main(args: Array[String]) {
    val logFile = "/usr/lib/spark/README.md" // Should be some file on your system
    //val sc = new SparkContext("local", "Simple App", "/usr/lib/spark",
    //  List("target/scala-2.10/simple-project_2.10-1.0.jar"))
    //val logData = sc.textFile(logFile, 2).cache()
    //val numAs = logData.filter(line => line.contains("a")).count()
    //val numBs = logData.filter(line => line.contains("b")).count()
    //println("Lines with a: %s, Lines with b: %s".format(numAs, numBs))
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
  }
}
