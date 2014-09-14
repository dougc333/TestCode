package com.example

import rx.lang.scala._

object ThreadingUtils {
   val generator: Observable[Int] = Observable.from(1 to 10)
  //change to AnyRef
  implicit class Hate(observable:Observable[Int]){
	  def debug(message: String) = {
        observable.doOnNext(value => {
        ThreadingUtils.debug(message, value)
       })
      }
  }
  
  def debug(message:String, value:Int)={
    println("debug:"+message+" value:"+value)
  }

}