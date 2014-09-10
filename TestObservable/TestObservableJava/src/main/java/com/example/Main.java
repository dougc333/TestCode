package com.example;

public class Main{
	public static void main(String []args){
		CoffeeShop cs = new CoffeeShop();
		cs.addObserver(new MyObserver("cust1"));
		cs.addObserver(new MyObserver("cust2"));
		cs.addObserver(new MyObserver("cust3"));
		cs.notifyCustomers();	
	}
}