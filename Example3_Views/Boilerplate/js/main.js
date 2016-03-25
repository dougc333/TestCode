
// In the first few sections, we do all the coding here.
// Later, you'll see how to organize your code into separate
// files and modules.
var TestView = Backbone.View.extend({
  render:function(){
    this.$el.html("attach to html w/jquery");
    return this;
  }
});

var tview = new TestView({el:"#container"});
tview.render();


