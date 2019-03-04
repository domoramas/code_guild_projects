// #guess_the_number
let num = Math.floor((Math.random()*21)+1);
let guessNum = 0;
let lastGuess = 0;
// let game = true;
let btn = document.querySelector('#btn');
console.log(num)

function reset() {
    num = Math.floor((Math.random()*21)+1);
    guessNum = 0;
    lastGuess = 0; 
    console.log(num);
    let message= document.getElementById("message");
    message.innerText ="";
    let btn2 = document.getElementById("btn2");
    let container_div = document.getElementById('container');
    container_div.removeChild(btn2);

}

btn.addEventListener('click', checkguess);

// 
// function to check the guess d
// 
function checkguess() {
    let guess = document.getElementById("guess");
    let userGuess = parseInt(guess.value);
    ++guessNum;
    let message = document.getElementById("message");{
        if (userGuess === num) {  
            message.innerText= `You won and it only took you ${guessNum} tries!`;
            guess.style.backgroundColor="";
            let btn2 = document.createElement("button");
            btn2.type = "button";
            btn2.setAttribute("class","btn btn-info");
            btn2.setAttribute("id","btn2");
            btn2.innerText = 'Play Again';
            let container_div = document.getElementById('container');
            container_div.appendChild(btn2);
            btn2.addEventListener('click', reset);
        }else if (userGuess !== num) {
            if (guessNum === 1) {
                if ((Math.abs(num - userGuess)) < 5)  {
                    lastGuess = userGuess;
                    message.innerText= "warm";
                    guess.style.backgroundColor= "darkgoldenrod";
                }else if ((Math.abs(num - userGuess)) >= 5) {
                    lastGuess = userGuess;
                    message.innerText="cold";
                    guess.style.backgroundColor= "lightskyblue"
                }
            } else {
                    if ((Math.abs(num - userGuess)) < (Math.abs(num -lastGuess))) {
                    lastGuess = userGuess;
                    message.innerText="Getting warmer, try again.";
                    guess.style.backgroundColor= "orange";
                    }else if ((Math.abs(num - userGuess)) > (Math.abs(num -lastGuess))) {
                    lastGuess = userGuess;
                    message.innerText="Getting colder, try again.";
                    guess.style.backgroundColor="skyblue"
                } 
            }
        }
    }; guess.value = "";
}

