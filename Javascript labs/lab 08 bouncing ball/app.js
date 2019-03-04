let cnv = document.getElementById('cnv');
let ctx = cnv.getContext('2d');

let ball = {
    radius: (Math.random()*20)+2,
    px: Math.random()*cnv.width,
    py: Math.random()*cnv.height,
    vx: (2*Math.random()-1)*20,
    vy: (2*Math.random()-1)*20
};
let balls = [];
// ctx.beginPath();
// ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
// ctx.fillStyle = 'green';
// ctx.fill()
let friction = .999;
let gravity = 2;
function main_loop() {
    let ctx = cnv.getContext("2d");
    ctx.fillStyle = "rgba(0, 0, 0, 0.1)";
    ctx.fillRect(0, 0, cnv.width, cnv.height);
    ctx.fillStyle = "blue";
    // ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
    // ctx.fill();
     if ((ball.px + ball.radius) > cnv.width){
         ball.px = (cnv.width - ball.radius);
         ball.vx *= friction;
         ball.vy *= friction;
         ball.vx *= -1;
     }else if ((ball.px - ball.radius) < 0) {
         ball.px= 0 +ball.radius;
         ball.vx *= friction;
         ball.vy *= friction;
         ball.vx *= -1;
     }if ((ball.py + ball.radius) > cnv.height) {
         ball.py = (cnv.height - ball.radius);
         ball.vx *= friction;
         ball.vy *= friction;
         ball.vy *= -1;
    }else if ((ball.py - ball.radius )< 0) {
         ball.py = ball.radius;
         ball.vx *= friction;
         ball.vy *= friction;
         ball.vy *= -1;
     }
     ball.py += ball.vy;
     ball.px += ball.vx;
     ball.vx *= friction;
     ball.vy *= friction;
     if (ball.py - ball.radius > 0 ) {
         ball.py += gravity;
     }else if (ball.py + ball.raidous < cnv.height) {
        ball.py += gravity;
     }

     ctx.beginPath();
     ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
     ctx.fill();
    window.requestAnimationFrame(main_loop);
}
window.requestAnimationFrame(main_loop);

