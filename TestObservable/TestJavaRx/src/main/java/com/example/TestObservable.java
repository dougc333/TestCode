//import rx.observable.*;

import rx.Observable;
 
public class TestObservable{


  public static void main(String []args){
	System.out.println("asdf");
	Observable.just(5,6,7,8).subscribe(new MySubscriber<Integer>());
	//endless stream 
	//Observable.just(5,6,7,8).repeat().subscribe(new MySubscriber<Integer>());
	
  }
  
  
}
