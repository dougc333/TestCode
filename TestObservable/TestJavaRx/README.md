https://github.com/ReactiveX/RxJava/wiki/Getting-Started

says to copy the dependencies into target/dependency....

$ mvn -f pom.xml dependency:copy-dependencies

mvn compile
run the HelloWorld program

there are some inconsistencies in the docs. 
this package is completely different than what is in the std scala libs. 

Scaladocs:
http://rxscala.github.io/scaladoc/index.html#package
rx.lang.scala.Observable

Javadocs:
http://reactivex.io/RxJava/javadoc/
rx.Observable

The Java rx.Observable class is different than the scala rx.lang.scala.Observable


Java rx.Observable.Observable<T> contains just("asdf") here:
http://reactivex.io/RxJava/javadoc/

The scala observable does not. 



