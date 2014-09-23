package com.example

import scala.concurrent._
import ExecutionContext.Implicits.global
import scala.concurrent.duration._
import scala.util._


//2 ways to declare Future, future method and via Promise
object TestFuture{

 //a Future is a future read
 //a Promise is a future write
 //these 2 objects have to work together
 //creating an immediate Future like Future(2) can cause errors in understanding
 //because there is no timeline or sequential causation of events. A promise write has to occur before a future read
 //which you dont see with val f = Future(10)
 def simpleFuture={   
   val f = Future(10)
   //onComplete causes second thread
   f onComplete{
     case Success(x)=>println("success x:"+x)
     case Failure(x)=>println("error:"+x)
   }
   val res = Await.result(f,0 nanos) 
   println(res+" thread:"+Thread.currentThread().getName()+ "num:"+Thread.activeCount())  
 }
 
 def simpleFuturePromise{
  val p = Promise[Int]()
  p.success(100)
  val f = p.future
  //f onComplete{
  //   case Success(x)=>println("success x:"+x)
  //   case Failure(x)=>println("error:"+x)
  //}
  println(Await.result(f, 0 nanos)+" "+Thread.currentThread().getName()+" num:"+Thread.activeCount())
 }

 //there is a programming style for Futures which is not to chain callbacks
 //this is unique to scala
 //http://docs.scala-lang.org/overviews/core/futures.html
 def futureAPI{

 }

 def main(args:Array[String]){
//   simpleFuture
   simpleFuturePromise
 }

}
