
var TestObj=Backbone.Model.extend({
   idAttribute: 'testId',
   urlRoot: "/test/testme",
   defaults:{
      testId:0
   },
   initialize:function(){
     console.log("TestObj initialize");
   },
   start:function(){
     console.log("start function");
   }
});

var Vehicle = Backbone.Model.extend({
   idAttribute: 'registrationNumber',
   urlRoot: "/api/vehicles",
   start:function(){
      console.log("Vehicle start");
   },
   validate :function(attrs){
      if(!attrs.registrationNumber)
         console.log("need value in registrationNumber");
   }    
});

var Car= Vehicle.extend({
  initialize:function(){
    Vehicle.prototype.initialize.apply(this, arguments);
  },
  start:function(){
    console.log("Car with registrationNumber:");
    console.log()
  }
});


//var car = new Car(registrationNumber:'XLI887', color:'Blue');
