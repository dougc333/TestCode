package com.example;

import com.google.common.util.concurrent.Service;
import com.google.common.util.concurrent.ServiceManager;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeoutException;

import com.google.common.util.concurrent.Service.Listener;
import java.util.concurrent.TimeUnit;
import com.google.common.collect.Lists;

/**
 * Service manager running BenchmarkService
 * Add jmx
 * Add quartz
 * Add jobs and tasks into service
 */
public class App 
{
	
    public static void main( String[] args )
    {
    	List<Service> services = Lists.<Service>newArrayList(new BenchmarkService());    	
        System.out.println( "Running services" );
        final ServiceManager serviceManager = new ServiceManager(services);
        Runtime.getRuntime().addShutdownHook(new Thread(){
        	public void run(){
        		System.out.println("run");
        		try {
					sleep(1000);
        			serviceManager.stopAsync().awaitStopped(5,TimeUnit.SECONDS);
				} catch (Exception e) {
					e.printStackTrace();
				}
        	}
        });
        serviceManager.startAsync();
              
    }
}
