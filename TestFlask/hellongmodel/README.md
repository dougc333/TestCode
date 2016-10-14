1) The simplest example for ngmodel is to set ngmodel to an input variable 
and then echo it to teh browser
2) buttonhide.html, buttonhide1.html the second example is to test using a button to add/hide content. You can't use separate
ng-controller = "mc" for each element and expect them to unify the state. You have to nest the divs. 
    controller functions are defined as $scope.functionName = function(){... some code...}
    they are called with parenthesis; ng-show="functionName()" 

3) route.html



