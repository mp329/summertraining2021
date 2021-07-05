
function sync(){
    var selectInputValue = document.getElementById("searchBox").value;
    console.log(selectInputValue);
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://192.168.56.101/cgi-bin/new.py?Number="+selectInputValue, true);
    xhr.send();
    xhr.onload = function (){
      var output = xhr.responseText;
      document.getElementById("container").innerHTML = output;
    }
  }   

