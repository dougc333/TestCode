package com.example;

import rx.*;


public class BlockingObservable {

	public static void main(String []args){
		rx.observables.BlockingObservable<Integer> blockingObservable = Observable.just(1,2,3,4,5).toBlocking();
		
	}
}
