package com.example;

import rx.*;
import rx.functions.Action1;

public class ObservableCreate {

  public static void main(String args[]){
	  Observable.create(new CreateObservable<Integer>()).subscribe(new Action1<Integer>() {
			@Override
		    public void call(Integer integer) {
		        
		    }
		});
  }
  
}
