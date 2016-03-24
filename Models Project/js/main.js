//vehicle

var Vehicle = Backbone.model.extend({
  idAttribute: "registrationNumber",
  urlRoot="/api/vehicles"
  validate: function(attrs){
     if (attrs.registrationNumber == null){
        console.log("invalid registrationNumber");
        return "vehicle not valid"; 
     }
  }),
  start:function(){
    console.log("vehicle start")
  }
});

var Car= Vehicle.extend({
  start:function(){
    console.log("car start:"+this.get("registrationNumber"));
  }
});

var car = new Car("registrationNumber":"XLI887", "color":"Blue");
car.vehicle.start();
car.validate();
car.start();

