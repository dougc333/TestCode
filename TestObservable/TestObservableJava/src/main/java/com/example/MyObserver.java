package com.example;

import java.util.Observable;
import java.util.Observer;

//models customer going to coffeeshop. can change name. leave observer
public class MyObserver implements Observer{
	private String name=null;
	private boolean atCoffeeShop=false;
	
	MyObserver(String n){
	  this.name=n;
	}
	
	@Override
	public void update(Observable o, Object arg) {
		// TODO Auto-generated method stub
		System.out.println("calling update callback for:"+name);
	}
		
}
