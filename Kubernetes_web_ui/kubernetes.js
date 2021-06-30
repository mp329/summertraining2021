
function sync(){
    let selectInputValue = document.getElementById("searchBox").value;
    console.log(selectInputValue);
    let xhr = new XMLHttpRequest();
    xhr.open("GET", "http://192.168.56.101/cgi-bin/k8s.py?var="+selectInputValue, true);
    xhr.send();
    xhr.onload = function (){
      let output = xhr.responseText;
      document.getElementById("container").innerHTML = output;
    }
  }   
  
let i = 0;
function gesture(){
  let ref = document.getElementById("image");
  console.log("call");
  ref.style.top = `${i}px`;
  i++;
  if(i === 630){
    i = 0;
  }
  setTimeout(gesture, 10); // setTimeout() function used to delay 
}
