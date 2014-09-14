package com.example

import rx.lang.scala._

package object threading{

 val generator:Observable[Int] = Observable.from(1 to 10)

 def debug(s:String)={
   println("s:"+"thread:"+Thread.currentThread().getName()+" num:"+Thread.activeCount() )
 }

}
