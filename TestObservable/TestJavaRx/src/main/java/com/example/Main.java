//package com.example;


public class Main{

  public static void main(String []args){
    ObservableState os1 = new ObservableState(100);
    ObserverUser user = new ObserverUser(os1);
    os1.addObserver(user);    
  }

}
