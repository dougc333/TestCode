package com.example

import rx.lang.scala._

class MySubscriber[Int] extends Subscriber[Int]{
  def onCompleted(){
    println("completed")
  }
  def onError(throwable:Throwable){
    println("error")
  }
  def onNext(x:Int){
    System.out.println("x:"+x)
  }
}
