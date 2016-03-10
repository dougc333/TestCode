package com.example;

import org.quartz.JobDetail;
import org.quartz.Scheduler;
import org.quartz.SchedulerException;
import org.quartz.SchedulerFactory;
import org.quartz.Trigger;
import static org.quartz.DateBuilder.evenMinuteDate;
import static org.quartz.JobBuilder.newJob;
import static org.quartz.TriggerBuilder.newTrigger;

import org.quartz.JobDetail;
import org.quartz.Scheduler;
import org.quartz.SchedulerFactory;
import org.quartz.Trigger;
import org.quartz.impl.StdSchedulerFactory;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Date;




public class TestQuartz {

	/*simpleExample1
	 * To use Quartz:
	 * 1) create a scheduler, job and trigger, add to scheduler and start scheduler. 
	 * 
	 * 
	 * 
	 */
	public void simpleExample1() throws Exception{
      SchedulerFactory schedFactory = new StdSchedulerFactory();
	  Scheduler sched= schedFactory.getScheduler();
		  
	  //Date runTime = evenMinuteDate(new Date());
      //change line to startAt(runTime) vs. startNow()
	  JobDetail job = newJob(HelloJob.class).withIdentity("myJob", "group1").build();

	  // Trigger the job to run now, and then every 40 seconds
	  Trigger trigger = newTrigger()
	  .withIdentity("myTrigger", "group1")
	  .startNow()
	  .build();
	  sched.scheduleJob(job, trigger);
			
	  sched.start();

	  Thread.sleep(1L); //time to execute, need to sleep this thread to get the other one to run
	  //shold be executing
      sched.shutdown();
      sched.clear();
      sched=null;
      job=null;
      trigger=null;
	}

	//simple trigger example
	public void simpleExample2(){
	  //
	  	
		
		
	}
	
	public void run() throws Exception{
		System.out.println("simpleExample1, schedule a HelloJob to run after 1ms sleep");
		simpleExample1();
	}
	
  public static void main(String []args) throws Exception{
	  TestQuartz tq = new TestQuartz();
	  tq.run();
  }
}
