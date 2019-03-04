let urlsList = ["https://www.slashfilm.com/", "https://www.cnn.com", "https://www.guitarcenter.com", "https://www.oregonlive.com", "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "https://i.kym-cdn.com/photos/images/original/000/276/668/ad3.jpg"];
let destination = urlsList[(Math.round(Math.random()*(urlsList.length)))];
console.log(destination);

function redirect(){
location.assign(destination);
}

function countdown5(){
    document.getElementById("timer").innerHTML = "5";

}
function countdown4(){
    document.getElementById("timer").innerHTML = "4";
    
}
function countdown3(){
    document.getElementById("timer").innerHTML = "3";
    
}
function countdown2(){
    document.getElementById("timer").innerHTML = "2";
    
}
function countdown1(){
    document.getElementById("timer").innerHTML = "1";
    
}

setTimeout(countdown5);
setTimeout(countdown4, 1000);
setTimeout(countdown3, 2000);
setTimeout(countdown2, 3000);
setTimeout(countdown1, 4000);
setTimeout(redirect, 5000);

