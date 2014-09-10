import rx.Subscriber;



class MySubscriber<Integer> extends Subscriber<Integer>{
		@Override
		public void onCompleted() {
			// TODO Auto-generated method stub
			System.out.println("Completed Observable.");
		}

		@Override
		public void onError(Throwable throwable) {
			// TODO Auto-generated method stub
	        System.err.println("Whoops: " + throwable.getMessage());
			
		}

		@Override
		public void onNext(Object arg0) {
			// TODO Auto-generated method stub
	        System.out.println("Got: " + arg0);		
		}
		  
	  }
	  

