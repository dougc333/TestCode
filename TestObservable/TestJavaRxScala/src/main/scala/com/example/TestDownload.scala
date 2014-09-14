package com.example

import rx.lang.scala._
import rx.lang.scala.Scheduler

object TestDownload {

  def customObservableNonBlocking(): Observable[String] = {
   Observable(
      subscriber => {
        // For simplicity this example uses a Thread instead of an ExecutorService/ThreadPool
        new Thread(new Runnable() {
          def run() {
            for (i <- 0 to 75) {
              if (subscriber.isUnsubscribed) {
                return
              }
              subscriber.onNext("value_" + i)
            }
            // after sending all values we complete the sequence
            if (!subscriber.isUnsubscribed) {
              subscriber.onCompleted()
            }
          }
        }).start()
      }
    )
  }
  
  
  
  def main(args:Array[String]){
    customObservableNonBlocking().subscribe(x=>println(x))    
    
  }
  
}