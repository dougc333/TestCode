package com.example;

public class DelayObject {
    int delay;
    
    
	public DelayObject(Long delay) throws InterruptedException{
		this.delay=delay.intValue();
		System.out.println("thread:"+Thread.currentThread().getName()+ " sleeping:"+ delay +" count:"+Thread.activeCount());
		Thread.yield();
		Thread.sleep(delay);
	}
	
	public int getDelay(){
		return delay;
	}
}
