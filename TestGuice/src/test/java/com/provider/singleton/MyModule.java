package com.provider.singleton;

import com.google.inject.AbstractModule;
import com.google.inject.Singleton;

@Singleton
public class MyModule extends AbstractModule{
 protected void configure(){
	 //.in(Singleton) is not the same as an annotation
	 bind(Person.class).toProvider(MyProvider.class).in(Singleton.class);;
	 bind(OtherPerson.class).toProvider(OtherProvider.class);
 }
}
