// #unit_converter.py lab


function conversion(e) {
    let num = document.getElementById("num");
    let n = num.value;
    let inUnit = document.getElementById("inUnit");
    let i = inUnit.value
    let outUnit = document.getElementById("outUnit");
    let o = outUnit.value;
    let toMeters = { ft: 0.3048, mi: 1609.34, m :1, km :1000, yd :0.9144, in: 0.0254};
    let convertedAnswer = document.getElementById("answer");
    let conversion = Number((n * toMeters[i]/toMeters[o]).toFixed(5));
    convertedAnswer.innerText= `${n} ${i} equals ${conversion} ${o}`;
}

let btn = document.querySelector('#btn');
btn.addEventListener('click', conversion);
