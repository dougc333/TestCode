package com.example;

import java.util.concurrent.Executor;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;

import com.google.common.util.concurrent.*;


public class BenchmarkService extends AbstractIdleService{

	public int fib(int n){
		if(n==0 || n==1) 
			return 1;
		return fib(n-1)+fib(n-2);
	}
	
	@Override
	protected void shutDown() throws Exception {
		// TODO Auto-generated method stub
		System.out.println("benchmark service shutdown");
	}

	@Override
	protected void startUp() throws Exception {
		// TODO Auto-generated method stub
		System.out.println("bencmark service startup");
		int result = fib(45);
		System.out.println("result:"+result);
	}
   
}
