package com.example.threading

import scala.io.Source
import java.io.{FileOutputStream, File}
import java.net.URL


import rx.lang.scala.{Subscription, Observer, Observable} 

object TestRx{

private val lastScript = "http://www.google.com"



def getAsyncUrl(urlString: String):Observable[Option[String]] = Observable {
    (observer: Observer[Option[String]]) => {
      val url = new URL(urlString)
      val urlCon = url.openConnection()
      urlCon.setConnectTimeout(5000)
      urlCon.setReadTimeout(5000)
      val io = Source.fromInputStream(urlCon.getInputStream)
      val result = Option(io.getLines().mkString.split("\n")(0))
      io.close()
      observer.onNext(result)
      observer.onCompleted()
     // Subscription()
    }
}


//val mUnsubscribe = CompositeSubscription() 

  def main(args:Array[String]){
    println("aa");
    val m = getAsyncUrl(lastScript).subscribe(x=>println(x))
    println("bb"); 
  }  


}