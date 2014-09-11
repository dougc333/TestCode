package com.example;

import rx.*;

//implement logic when to call onNext(), onError(), onComplete() by using create()
//demo only
public class CreateObservable<Integer> implements Observable.OnSubscribe<Integer>{

	@Override
	public void call(Subscriber<? super Integer> arg0) {
	  // TODO Auto-generated method stub
	  Subscriber subscriber = (Subscriber) arg0;
	  try{
	    if(!subscriber.isUnsubscribed()){
	      for(int i=0;i<5; i++){
	        subscriber.onNext(i);
	      }
	      subscriber.onCompleted();
	    }
	  }catch(Exception e){
	    subscriber.onError(e);
	  }
	}
}
