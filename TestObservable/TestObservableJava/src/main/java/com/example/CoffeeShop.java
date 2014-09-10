package com.example;

import java.util.Observable;

public class CoffeeShop extends Observable{
	
	public  void enterCoffeeShop(MyObserver obs){
      addObserver(obs);
	}
	
	public void notifyCustomers(){
		setChanged();
		notifyObservers();
	}
	
}
