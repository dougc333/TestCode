package com.example.threading

object Test{
 def main(args:Array[String]){
   println("asdf")
   val foo = generator
   generator.subscribe(x=>println(x))
   
 }
}
