
//package com.example;

import java.util.Observable;

//contains list of observers
public class ObservableState extends Observable{
  private int val=0;

  public ObservableState(int v){
    this.val = v;
  }

  public void setValue(int v){
    this.val=v;
    setChanged();
    notifyObservers();
  }

  public int getValue(){
    return val;
  }
}
