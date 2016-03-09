package com.provider.singleton;

import com.google.inject.Provider;
import com.google.inject.Singleton;

//singleton annotation implies thread safe, apply @singleton to impl classes
@Singleton
public class MyProvider implements Provider<Person>{
    @Singleton
	public Person get(){
	   System.out.println("calling MyProvider.get()");
	   return new Person("camille",100);
   }
}
