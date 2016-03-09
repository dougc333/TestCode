package com.provider.singleton;

import com.google.inject.Guice;
import com.google.inject.Injector;


//demonstrate a singleton where you create the object once
//only one call to MyProvider.get() or service provider interface
public class Test {

	//this is ok but dangerous. I dont get a NPE but I can get incorrect behavior
	public static void main(String []args){
		Injector injector = Guice.createInjector(new MyModule());
		Person a = injector.getInstance(Person.class);
		System.out.println("person name:"+a.getName()+" Person age:"+a.getAge());
		Person a1 = injector.getInstance(Person.class);
		System.out.println("person name:"+a.getName()+" Person age:"+a.getAge());
		if(a1==null){
			System.out.println("a1 null");
		}
	
		OtherPerson b = injector.getInstance(OtherPerson.class);
		OtherPerson b1 = injector.getInstance(OtherPerson.class);
		
		
	}
	
}
//output, not only one call to myprovider.get w/singleton
//calling MyProvider.get()
//calling people ctor
//person name:camille Person age:100
//person name:camille Person age:100
//calling OtherProvider.get()
//calling OtherProvider.get()