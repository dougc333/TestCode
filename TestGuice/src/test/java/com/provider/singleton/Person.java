package com.provider.singleton;

import com.google.inject.Singleton;

@Singleton
public class Person {
	private  String name;
	private Integer age;
	
	public Person(String name, Integer age){
		System.out.println("calling people ctor");
		this.name=name;
		this.age=age;
	}
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public Integer getAge() {
		return age;
	}
	public void setAge(Integer age) {
		this.age = age;
	}
	
	
}
