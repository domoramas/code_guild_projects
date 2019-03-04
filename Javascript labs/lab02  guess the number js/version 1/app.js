// #guess_the_number
let num = Math.floor(Math.random()*21);

let guess = parseInt(prompt(`What number am thinking of between 1 and 20? ${num} `));
let guessNum = 0
let lastGuess = 0
let game = true;
while (game) {   
    if (guess === num) {
        ++guessNum;
        game = false; 
        alert(`You won and it only took you ${guessNum} tries!`);
    }else if (guess !== num) {
        if (guessNum < 1) {
            if (guess < num) {
                ++guessNum;
                lastGuess = guess;
                guess = parseInt(prompt("too low, try again"));
            }else if (guess > num) {
                ++guessNum;
                lastGuess = guess;
                guess = parseInt(prompt("too high, try again"));
            }
        } else {
            if (Math.abs(num - guess) < Math.abs(num -lastGuess)) {
                ++guessNum;
                lastGuess = guess;
                guess = parseInt(prompt("Getting warmer, try again."));
            }else if (Math.abs(num - guess) > Math.abs(num -lastGuess)) {
                ++guessNum;
                lastGuess = guess;
                guess = parseInt(prompt("Getting colder, try again."));
            }
        }  
    }
}