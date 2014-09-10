//package com.example;

import java.util.Observable;
import java.util.Observer;

public class ObserverUser implements Observer{
  private ObservableState os = null;
  
  public ObserverUser(ObservableState os){
    this.os = os;
  }

  public void update(Observable ob, Object obj){
    if(ob==os){
      System.out.println("os getValue:"+os.getValue());
    }
  }

}
