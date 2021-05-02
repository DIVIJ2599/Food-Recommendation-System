var Loaditems= function(){
  debugger;
  var quotes = new Array('Cheese Maggi','Chicken Tikka','Masala Maggi','Paneer Tikka','Veg Maggi');
  var i;

  for (i=0;i<quotes.length;i++){
    var newquotes = quotes[Math.floor(Math.random() * quotes.length)];
    document.getElementById('itemshare').innerText = newquotes;
  }
};