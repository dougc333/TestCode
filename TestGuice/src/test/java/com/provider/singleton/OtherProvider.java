package com.provider.singleton;

import com.google.inject.Provider;

public class OtherProvider implements Provider<OtherPerson>{
	   public OtherPerson get(){
		   System.out.println("calling OtherProvider.get()");
		   OtherPerson op=new OtherPerson();
		   op.setName("Sam");
		   op.setAge(10);
		   return op;
	   }
	}