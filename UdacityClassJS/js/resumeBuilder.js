
var bio={
  "name":"James Doe",
  "role":"Web Programmer",
  "contacts":{
       "mobile":"111-11-0000",
       "email":"jdoe@gmail.com",
       "github":"johndoe",
       "twitter":"@johndoe",
       "location":"San Francisco"
   },
   "welcomeMessage":"welcome thee this is more text, text..text hello hi hi hi hi hi hi hi hi hi",
    "skills":["program1","program2","program3","program4"],
    "bioPic":"images/fry.jpg"
}

var work={
   "jobs":[
    {
     "employer":"Planet Express",
     "title":"Delivery Boy",
     "dates":"2002",
      "description":"move boxes high low middle up down everywhere move move move box box big small medium any size"
    },
    {
     "employer":"PizzaPlace",
     "title":"Pizza Delivery Boy",
     "dates":"2200",
     "description":"deliver pizzas bread edibles food drink coke to hungry people all over with car bike foot everyday"
    }
    ]
}

var education={
  "schools":[
   {
      "name": "Nova Southeastern",
      "city": "Ft Lauderdale",
      "degree": "Masters",
      "majors":"CS",
      "dates": "2013",
      "url":"http://www.example.com/"
    }, 
    {
       "name": "Eckerd College",
       "city": "St Petersburg Fla",
       "degree":"BS",
       "majors":"CS",
       "url":"www.example.com/"
    }
   ],
   "online classes":[
    {
       "title":"Javascript",
       "school":"Udacity",
       "dates":"2014",
       "url":"www.udacity.com"
    }
    ]
}
var projects={
   "name":"p1"
}
//$("#main").append(work["position"]);
//$("#main").append(education.name);
var formattedName = bio.name
var formattedRole = "web programmer";
var HTMLheaderName = HTMLheaderName.replace("%data%", formattedName);
var HTMLheaderRole = HTMLheaderRole.replace('%data%', formattedRole);
$("#header").prepend(HTMLheaderName);
$("#header").append(HTMLheaderRole);
var HTMLmobile = HTMLmobile.replace("%data%",bio.contacts.mobile);
$("#header").append(HTMLmobile);
var HTMLemail=HTMLemail.replace("%data%",bio.contacts.email);
$("#header").append(HTMLemail);
var HTMLgithub = HTMLgithub.replace("%data%",bio.contacts.github);
$("#header").append(HTMLgithub);
var HTMLtwitter = HTMLtwitter.replace("%data%",bio.contacts.twitter);
$("#header").append(HTMLtwitter);
var HTMLbioPic = HTMLbioPic.replace("%data%",bio.bioPic);
$("#header").append(HTMLbioPic);
var HTMLwelcomeMsg = HTMLwelcomeMsg.replace("%data%",bio.welcomeMessage);
$("#header").append(HTMLwelcomeMsg);
if (bio.skills.length > 0){
  $("#header").append(HTMLskillsStart);
  for (var i=0;i<bio.skills.length;i++){
      var temp = HTMLskills.replace("%data%",bio.skills[i]);
      $("#header").append(temp);
  }
}




//test prototype

function Animal(name){
  this.name = name;
  this.properties = {"fur":"no", "teeth":"100", "color":"red"};
  this.bankaccounts=["chase","amex","wf","bofa"];
}

Animal.prototype.speak = function(){
  console.log("name:"+this.name);
}

function Cat(name) {
    Animal.call(this,name);
    this.parentba = Animal.bankaccounts;
    //this.bankaccounts=["a","b"];
}

Cat.prototype = new Animal()
var cat = new Cat('Kitty');
cat.speak();

console.log(cat.bankaccounts);

  work.jobs.forEach(function(jobItem){
     console.log(jobItem)
     $("#workExperience").append(HTMLworkStart);
     //$("#workExperience").append("LLLLLL");
     var HTMLworkEmp = HTMLworkEmployer.replace("%data%",jobItem.employer);
     var HTMLworkTit = HTMLworkTitle.replace("%data%",jobItem.title);
     $(".work-entry:last").append(HTMLworkEmp+HTMLworkTit);

     var HTMLworkda = HTMLworkDates.replace("%data%", jobItem.dates);
     $(".work-entry:last").append(HTMLworkda);
     var HTMLworkDesc = HTMLworkDescription.replace("%data%",jobItem.description);
     $(".work-entry:last").append(HTMLworkDesc);
  });

$(document).click(function(loc){
  console.log(loc.clientX);
  console.log(loc.clientY);

});


$("#main").append(internationalizeButton);

function inName(firstName, secondName){


}