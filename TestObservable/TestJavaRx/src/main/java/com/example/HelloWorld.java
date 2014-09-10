//package com.example;

import rx.*;
import rx.exceptions.*;
import rx.functions.*;
import rx.internal.operators.*;
import rx.internal.util.ScalarSynchronousObservable;
import rx.observables.*;
import rx.observers.SafeSubscriber;
import rx.plugins.*;
import rx.schedulers.*;
import rx.subjects.*;
import rx.subscriptions.Subscriptions;



class HelloWorld{
 
  public static void hello(String ... names){
    Observable.from(names).subscribe(new Action1<String>(){

      @Override
      public void call(String s){
        System.out.println("Hello "+s);
      }
    });
  }

  public static void main(String []args){ 
    hello("ben","asdf");
  }

}
