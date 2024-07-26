var calculation='';

function display(){
  document.querySelector(".js-calculation").innerHTML=calculation;
}

function updateCalc(buttonPress){
  calculation+=buttonPress;
  display();
}

function evaluate()
{
  calculation=eval(calculation);
  display();
}

function clearCalc()
{
  calculation='';
  display();
}