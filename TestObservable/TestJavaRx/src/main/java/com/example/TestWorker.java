package com.example;

import rx.*;
import rx.Scheduler.Worker;
import rx.functions.Action0;
import rx.schedulers.Schedulers;

public class TestWorker {

	public static void main(String args){
	  final Worker worker = Schedulers.newThread().createWorker();
	  worker.schedule(new Action0(){
		  @Override 
		  public void call(){
			  //download urls
			  worker.schedule(this);
		  }
		  
	  });
	  //how to test for unsubscribe?
	  worker.unsubscribe();
	}
}
