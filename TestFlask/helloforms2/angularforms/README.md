1) angular module has 1 instance of App. Even if you make up a nonexistent name
it still uses the current name. There is no error message. Even if you look
in the debugger there is no error message on noApp being undefined. 


models/views/controllers:
https://docs.angularjs.org/api/ng/type/ngModel.NgModelController

all the AngularForms are stored in Forms.formController
you can activate js functions on submit; the default action of page refresh
can be overridden

https://docs.angularjs.org/api/ng/directive/form
