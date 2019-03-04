function clock(){
    let time = new Date();
    document.getElementById("clock").innerHTML = time.toLocaleTimeString();
}
// starts clock when page loads
let time = new Date();
    document.getElementById("clock").innerText = time.toLocaleTimeString();
    // refreshes every second
let myClock = setInterval(clock, 1000);
//hides and shows the clock
let clockBtn = document.getElementById("clockbtn");

clockBtn.addEventListener("click", function(){
    document.getElementById("clock").style.display = "block";
    document.getElementById("stopwatcher").style.display = "none";
    document.getElementById("stopwatch").style.display = "none";
    document.getElementById("countdown-timer").style.display = "none";
    document.getElementById("countdown").style.display = "none";
})


// STOPWATCH!!!!!!!!!!!!!!!!!!!!!
let swBtn = document.getElementById("sw-btn");
swBtn.addEventListener('click', function(){
    document.getElementById("clock").style.display = "none";
    document.getElementById("stopwatcher").style.display = "flex";
    document.getElementById("stopwatch").style.display = "block";
    document.getElementById("countdown-timer").style.display = "none";
    document.getElementById("countdown").style.display = "none";
})

// sets the timer to 0's when page loads
let swtime = new Date();
swtime.setHours(0,0,0,0);
let h = swtime.getHours();
let m = swtime.getMinutes();
let s = swtime.getSeconds();
h = checkTime(h);
m = checkTime(m);
s =checkTime(s);
document.getElementById("stopwatch").innerText = `${h} : ${m} : ${s}`

function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
}
// adds a second to the timer
function stopWatch() {
    swtime.setSeconds(swtime.getSeconds() +1);
    let h = swtime.getHours();
    let m = swtime.getMinutes();
    let s = swtime.getSeconds();
    h = checkTime(h);
    m = checkTime(m);
    s =checkTime(s);
    document.getElementById("stopwatch").innerText = `${h} : ${m} : ${s}`;
}
// starts the timer

let startBtn = document.getElementById("start");

startBtn.addEventListener("click", function(){
    startTimer = setInterval(stopWatch, 1000);
    startBtn.disabled = true;
});

//  stops timer
let stopBtn = document.getElementById("stop");

stopBtn.addEventListener("click", function(){
    clearInterval(startTimer);
    startBtn.disabled = false;
});


//  prints lap times on the page in an unordered list
let lapBtn = document.getElementById("lap");
let lapList = document.getElementById("laptimes");
lapBtn.addEventListener("click", lapTime)

function lapTime(){
    let laps = document.createElement("li");
    let h = swtime.getHours();
    let m = swtime.getMinutes();
    let s = swtime.getSeconds();
    h = checkTime(h);
    m = checkTime(m);
    s =checkTime(s);
    laps.innerText = `${h} : ${m} : ${s}`;
    lapList.appendChild(laps);
}
// resets the stopwatch to 0's and removes laps
let resetBtn = document.getElementById("reset");

resetBtn.addEventListener("click", function(){
    let laps = document.getElementsByTagName("li");
    for (let i=(laps.length -1); i >= 0; i--){
        console.log(i);
        lapList.removeChild(laps[i])
    };
    swtime.setHours(0,0,0,0);
    clearInterval(startTimer);
    document.getElementById("stopwatch").innerText = `${h} : ${m} : ${s}`;

})
let timerTime = document.getElementById("countdown-time"); //this is the text input field
let timeUnit = document.getElementById("timeunit");// this is the drop down unit field
let countDown = document.getElementById("countdown"); // this is the h1 where the countdown time will display
let enterBtn = document.getElementById("enter-btn"); // this is the enter button for the timer
let cdTime = new Date();
cdTime.setHours(0,0,0,0);

//  opens up the timer
let timerBtn = document.getElementById("timer");

timerBtn.addEventListener("click", function(){
    document.getElementById("countdown-timer").style.display = "flex";
    let h = cdTime.getHours();
    let m = cdTime.getMinutes();
    let s = cdTime.getSeconds();
    h = checkTime(h);
    m = checkTime(m);
    s =checkTime(s);
    countDown.innerText = `${h} : ${m} : ${s}`;
    document.getElementById("countdown").style.display = "block";
    document.getElementById("clock").style.display = "none";
    document.getElementById("stopwatcher").style.display = "none";
    document.getElementById("stopwatch").style.display = "none";
    timerTime.style.display ="flex";
    timeUnit.style.display= "flex";
    enterBtn.style.display= "flex";
})




// function to set up the timer
function timer(){
    let countdownTime = parseInt(timerTime.value);
    if (isNaN(countdownTime)) {
        output.innerText= "invalid entry";
    }else {
    if (timeUnit.value == "hr"){
        cdTime.setHours(countdownTime,0,0,0)
    }else if (timeUnit.value == "min") {
        cdTime.setHours(0,countdownTime,0,0)
    }else if (timeUnit.value == "sec"){
        cdTime.setHours(0,0,countdownTime,0)
    }let h = cdTime.getHours();
    let m = cdTime.getMinutes();
    let s = cdTime.getSeconds();
    h = checkTime(h);
    m = checkTime(m);
    s =checkTime(s);
    countDown.innerText = `${h} : ${m} : ${s}`;
    timerTime.value= "";
    document.getElementById("countdown").style.display ="block";
    document.getElementById("countdown").style.background= "whitesmoke";
    timerTime.style.display ="none";
    timeUnit.style.display= "none";
    enterBtn.style.display= "none";
    enterBtn.disabled = true;
    }
}


function countItDown(){
        interval =setInterval(function(){
        cdTime.setSeconds(cdTime.getSeconds() -1);
        let h = cdTime.getHours();
        let m = cdTime.getMinutes();
        let s = cdTime.getSeconds();
        h = checkTime(h);
        m = checkTime(m);
        s =checkTime(s);
        countDown.innerText = `${h} : ${m} : ${s}`;
        if (h == 0 && m == 0 && s == 0){
            clearInterval(interval);
            document.getElementById("countdown").style.background = "red";
            timerTime.style.display ="flex";
            timeUnit.style.display= "flex";
            enterBtn.style.display= "flex";
            enterBtn.disabled = false;
        }
    } , 1000)}


enterBtn.addEventListener("click", timer);
enterBtn.addEventListener("click", countItDown);

`$('.slide').on('click', function(){
    $('#fade-in').toggleClass('show');
})`;
