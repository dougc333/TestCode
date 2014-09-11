package com.example;

import rx.Subscriber;

class MySubscriber<Integer> extends Subscriber<Integer>{
		@Override
		public void onCompleted() {
			// TODO Auto-generated method stub
			System.out.println("onComplete");
		}

		@Override
		public void onError(Throwable throwable) {
			// TODO Auto-generated method stub
	        System.err.println("Whoops: " + throwable.getMessage());
			
		}

		@Override
		public void onNext(Object arg0) {
			// TODO Auto-generated method stub
	        System.out.println("onNext: " + arg0);		
		}
		  
	  }
	  

