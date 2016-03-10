package com.example;

import java.util.concurrent.BlockingDeque;
import java.util.concurrent.TimeUnit;

import com.google.common.base.Optional;
import com.google.common.base.Preconditions;
import com.google.common.collect.Queues;

//import com.codahale.metrics.*;


public class TestQueue<T>  {

  private final int capacity;
  private final long timeout;
  private final TimeUnit timeoutTimeUnit;
  private final BlockingDeque<T> blockingDeque;
  private final Optional<QueueStats> queueStats;
  
  private TestQueue(Builder<T> builder){
	Preconditions.checkArgument(this.capacity>0);
	Preconditions.checkArgument(this.timeout>0);
	
	this.capacity=builder.capacity;
    this.timeout = builder.timeout;
    this.timeoutTimeUnit = builder.timeoutTimeUnit;
    this.blockingDeque = Queues.newLinkedBlockingDeque(builder.capacity);
    
    this.queueStats = builder.ifCollectStats ? Optional.of(new QueueStats()) : Optional.<QueueStats>absent();
  }
    
  boolean put(T record) throws InterruptedException{
    boolean offered = this.blockingDeque.offer(record,this.timeout, this.timeoutTimeUnit);
      //if(this.queueStats.isPresent()){
     //	  this.queueStats.get().putsRateMeter.mark();
      //}
    return offered;
    }
    
  public T get() throws InterruptedException{
    T record = this.blockingDeque.poll(this.timeout, this.timeoutTimeUnit);
      return record;
  }
  
  public Optional<QueueStats> stats(){
	return this.queueStats;
  }
  
  public void clear(){
	this.blockingDeque.clear();  
  }
  
  public static <T>Builder<T> newBuilder(){
	return new Builder<T>();
  }
  
  public static class Builder<T>{
    private int capacity;
    private long timeout;
    private TimeUnit timeoutTimeUnit;
    private boolean ifCollectStats;

    public Builder<T> hasCapacity(int capacity){
      this.capacity=capacity;
      return this;
    }
    
    public Builder<T> useTimeout(long timeout){
      this.timeout= timeout;
      return this;
    }
    
    public Builder<T> useTimeoutTimeUnit(TimeUnit timeoutTimeUnit){
      this.timeoutTimeUnit = timeoutTimeUnit;
      return this;
    }
    
    public TestQueue<T> build(){
      return new TestQueue<T>(this);	
    }
  }
	
  public class QueueStats{
	public static final String QUEUE_SIZE="queueSize";
	public static final String FILL_RATIO = "fillRatio";
	public static final String PUT_ATTEMPT_RATE = "putAttemptRate";
	public static final String GET_ATTEMPT_RATE="getAttemptRate";
	public static final String PUT_ATTEMPT_COUNT="putAttemptCount";
	public static final String GET_ATTEMPT_COUNT="getAttemptCount";
	
	//private final Gauge<Integer> queueSizeGauge;
	//private final Gauge<Double> fillRatioGauge;
	//private final Meter getRateMeter;
	//private final Meter putRateMeter;
	
	public QueueStats(){
	  //this.queueSizeGauge = new Gauge<Integer>(){
	//	@Override
	//	public Integer getValue(){
	//	  return blockingDeque.size();
	//	}
	 // };
	//this.fillRatioGauge=new Gauge<Double>{};
	//this.putRateMeter = new Meter();
	//this.getRateMeter = new Meter();
	}
	
	public int queueSize(){return 0;}
	public double fillRatio(){return 0.0;}
	public double putAttemptRate(){return 0.0;}
	public long putAttemptCount(){return 0;}
	public double getAttemptRate(){return 0.0;}
	public long getAttemptCount(){return 0L;}
	public void registerAll(){}
	public String toString(){return "";}
  }
  
	
}
