package com.example.threading

import com.example.ThreadingUtils._
import rx.lang.scala.schedulers.NewThreadScheduler
import rx.lang.scala._
import rx.lang.scala.Scheduler
object Test{
  
 
 def main(args:Array[String]){
   
  // val foo = generator
   println("simple observable,map")
   
   gen.map(x=>x+1).subscribe(x=>println(x))
    
  // gen.flatMap(n => Observable.from( n*2)).subscribe(x=>println("subscribe:"+x))
   
   println("simple subscribe 1 threads blocks")
   generator.subscribe(x=>println(x))
//   println("add 2 more thread")
   generator.subscribeOn(IOScheduler).subscribe(x=>println(x))
//   println("and no more after processor limit")
//   generator.subscribeOn(IOScheduler).subscribe(x=>println(x))
   //println("observeOn IOScheduler")
   //generator.map(x=>println("mapping:"+x).observeOn( IOScheduler).subscribe(x=>println(x))
   //println("observeOn IOScheduler")
   //generator.map(x=>println("mapping:"+x).observeOn( ComputationScheduler).subscribe(x=>println(x))
   //println("observeOn TrampolineScheduler")
   //generator.map(x=>println("mapping:"+x).subscribeOn(TrampolineScheduler).subscribe(x=>println(x))
   //println("observeOn NewThreadScheduler1")
   //generator.observeOn(NewThreadScheduler()).subscribe(x=>println(x))
   //println("observeOn NewThreadScheduler2")
   //generator.observeOn(NewThreadScheduler()).subscribe(x=>println(x))
   //println("observeOn NewThreadScheduler3")
   //generator.observeOn(NewThreadScheduler()).subscribe(x=>println(x))
 
 }
 
}