package com.example;

import rx.*;
import rx.functions.Action1;
import rx.functions.Func1;

import java.util.concurrent.*;

public class Timer {
  static CountDownLatch latch = new CountDownLatch(50);
     
  public static void noDebug() throws InterruptedException{
	  Observable.interval(1,TimeUnit.SECONDS).subscribe(new Action1<Long>(){
	      public void call(Long counter){
	        latch.countDown();
	        System.out.println("Timer Secs:"+counter);
	      }
		});
		
		latch.await();  
  }
  
  public static void debugTimer() throws InterruptedException{
	  Observable.interval(1,TimeUnit.SECONDS).map(new Func1<Long,Long>(){
		  @Override
		  public Long call(Long i){
		    System.out.println(Thread.currentThread().getName());
		    return i;
		  }
	  }).subscribe(new Action1<Long>(){
	      public void call(Long counter){
	        latch.countDown();
	        System.out.println("Timer Secs:"+counter);
	      }
		});
		
		latch.await();  
  }
  
  public static void debugSeq() {
	  Observable.just(1,2,3,4,5).map(new Func1<Integer,Integer>(){
		  @Override
		  public Integer call(Integer i){
			  System.out.println(Thread.currentThread().getName());
			  return i;
		  }
	  }).subscribe(new Action1<Integer>(){
		  @Override
		  public void call(Integer i){
			  System.out.println("onNext: " + i);
		  }
	  });
  }
  
  
  
  
  //parallel with observeOn vs. subscribeOn
  public static void debugMap() throws InterruptedException{
	  Observable.just(1,2,3,4,5,6,7,8,9,10);
	  
	  
  }
  
  public static void main(String args[]) throws InterruptedException{
	//debugTimer();
	  //debugSeq();
	debugMap();
  }
}
