package com.example

import rx.lang.scala.schedulers.IOScheduler
import rx.lang.scala.Observable
import language.implicitConversions

/**
 * Do all the registration / observation stuff:<br>
 *
 * - observe on main thread<br>
 * - subscribe on new thread<br>
 * - make it compliant with Scala notification<br>
 *
 * @param o the observable to transform
 * @tparam T the type of the observable
 */
class RxThread[T](o:Observable[T]) {
   def execAsync[T] = {
    o.subscribeOn(IOScheduler)
      .observeOn(IOScheduler)
      .materialize
  }
}

 /**
 * Convert implicitly a Java Observable in a Scala Observable.
 */
object RxThread {
implicit def Observable2Notification[T](o: Observable[T]) = new RxThread(o)
}