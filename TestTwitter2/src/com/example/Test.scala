package com.example

import org.apache.spark._
import org.apache.spark.streaming.StreamingContext
import org.apache.spark.streaming.Duration
import org.apache.spark.streaming.Seconds

import org.apache.spark.streaming.twitter._

object Test{
  
	def main(args:Array[String]){
	 val sparkConf = new SparkConf();
	 println(sparkConf.toString())
	 System.setProperty("twitter4j.oauth.consumerKey", "eFIaiOuxsny01VVQ2QWISK1Mw")
     System.setProperty("twitter4j.oauth.consumerSecret", "gDQI5EiCMJJaaNI8XVNhfZXwuCOYfeJ3XsOUNHvsXqgq0Hoj9T")
     System.setProperty("twitter4j.oauth.accessToken", "76976448-Otz8w4yMKx6yCEWTH3dNTfuF8LYeLgqdoDrcl0oBK")
     System.setProperty("twitter4j.oauth.accessTokenSecret", "NFPFe2EzuKWuzRKmY1RENUBfQzGeGbAS1JzjX3Eu3GwDE")
       //scaladocs not accurate, follow holden's exampple
	 val stream = new StreamingContext("local","Test", Seconds(1))
     val tweets= TwitterUtils.createStream(stream,None)
	 tweets.print()
	 //get hashtags
	 //val statuses = tweets.map(status=>status.getText())
	 //println("statuses:"+statuses)
	 //val words = statuses.flatMap(status=>status.split(" "))
	 //val hashtags = words.filter(word=>word.startsWith("#"))
	 //println(hashtags)
	 
	 stream.start()
	 println("+++++++++++++++++++++++++++++");
	 stream.awaitTermination()
       
	} 
  
}