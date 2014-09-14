package com.example

import rx.lang.scala._

object ThreadingUtils {
   val gen: Observable[Int] = Observable.from(1 to 10)
  //change to AnyRef
  implicit class Hate(observable:Observable[Int]){
	  def debug(message: String) = {
        observable.doOnEach(value => {
        println("bbbb");
        //ThreadingUtils.debug(message)
       })
      }
  }
  
  def debug(message:String)={
    println("aaaaa")
    println("debugccc:"+message+" thread:"+Thread.currentThread().getName()+" numThreads:"+Thread.activeCount())
  }

}