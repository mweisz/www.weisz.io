function showGreeting(){

    var d = new Date();
    var hour = d.getHours();

    var greeting = document.getElementById("greeting");

    if (hour < 4) {
      greeting.innerHTML = "Good Night";
    } else if (hour < 11) 
    {
      greeting.innerHTML = "Good Morning";
    } else if (hour < 17) 
    {
        greeting.innerHTML = "Welcome";
    } else if (hour < 23) 
    {
        greeting.innerHTML = "Good Evening";
    } else {
      greeting.innerHTML = "Good Night";
    }
} 


showGreeting();
