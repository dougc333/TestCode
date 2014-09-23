package com.example


object DelayObject{

  def main(){
   println("delayobject object"+Thread.currentThread.getName())
   Thread.sleep(10000)
  }

}


class DelayObject{
  def print={
    println("delay:"+Thread.currentThread.getName())
  }
}
