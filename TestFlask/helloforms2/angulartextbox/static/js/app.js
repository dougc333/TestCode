'use strict';


var myApp = angular.module('myApp',['ngRoute']);

myApp.config(['$routeProvider', function($routeProvider){
	$routeProvider.when('/',{templateUrl:'static/partials/index.html',}).
	when('about',{templateUrl:'static/partials/about.html',}).
	otherwise({
	  redirectTo: '/'
	});


}]);

