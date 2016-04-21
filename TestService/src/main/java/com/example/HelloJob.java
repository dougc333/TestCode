package com.example;

import java.util.Date;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.quartz.Job;
import org.quartz.JobExecutionContext;
import org.quartz.JobExecutionException;

public class HelloJob implements Job{

	public HelloJob(){}
	
	@Override
	public void execute(JobExecutionContext arg0) throws JobExecutionException {
		System.out.println("Hello Job");
	}

}
