		
// In the first few sections, we do all the coding here.
// Later, you'll see how to organize your code into separate
// files and modules.

var Vehicle = Backbone.Model.extend({

	idAttribute: "registrationNumber",

	urlRoot: "/api/vehicles",

	validate: function(attrs){
		if (!attrs.registrationNumber)
			return "Vehicle is not valid.";
	},

	start: function(){
		console.log("Vehicle started.");
	}
});

var Vehicles = Backbone.Collection.extend({
	Model: Vehicle
});

var Car = Vehicle.extend({
	start: function(){
		console.log("Car with registration number " + this.get("registrationNumber") + " started.");
	}
});

var VehicleView = Backbone.View.extend({
	tagName: "li",

	className: "vehicle",

	events: {
		"click .delete": "onDelete",
	},

	render: function() {
		var source = $("#vehicleTemplate").html();
		var template = _.template(source);

		this.$el.html(template(this.model.toJSON()));
		this.$el.attr("data-color", this.model.get("color"));

		return this;
	},

	onDelete: function(){
		this.remove();
	}
});

var VehiclesView = Backbone.View.extend({
	id: "vehicles",

	tagName: "ul",

	initialize: function(){
		// We pass "this" as the third argument so inside
		// onVehicleAdded method, we can access it. If 
		// you don't set the "this" here, and you access
		// "this" inside onVehicleAdded, it won't be pointing
		// to the view itself. This is how Javascript works.
		bus.on("newVehicle", this.onNewVehicle, this);
	},

	render: function(){
		this.collection.each(function(vehicle){
			var vehicleView = new VehicleView({ model: vehicle });
			this.$el.append(vehicleView.render().$el);
		}, this); // note the reference to this here. When you set
		// the "this" pointer here (as the second argument to the 
	    // each method, you'll be able to access "this" inside the 
	    // callback function in the each method:
	    //
	    // this.$el.append(...)

		return this;
	},

	onNewVehicle: function(registrationNumber){
		var car = new Car({ registrationNumber: registrationNumber });
		var vehicleView = new VehicleView({ model: car });
		this.$el.prepend(vehicleView.render().$el);
	}
});

var NewVehicleView = Backbone.View.extend({
	events: {
		"click .add": "onAdd"
	},

	render: function(){
		var source = $("#newVehicleTemplate").html();
		var template = _.template(source);

		this.$el.html(template());

		return this;
	},

	onAdd: function(){
		var input = this.$el.find(".registration-number");

		var registrationNumber = input.val();
		bus.trigger("newVehicle", registrationNumber);

		// It's the responsibility of this view to clear its text box
		input.val("");
	}
});

var bus = _.extend({}, Backbone.Events);

var vehicles = new Vehicles([
	new Car({ registrationNumber: "XLI887", color: "Blue" }),
	new Car({ registrationNumber: "ZNP123", color: "Blue" }),
	new Car({ registrationNumber: "XUV456", color: "Gray" })
]);

$("#container")
	.append(new NewVehicleView().render().$el)
	.append(new VehiclesView({ collection: vehicles }).render().$el);


