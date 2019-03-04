// #unit_converter.py lab
let toMeters = { ft: 0.3048, mi: 1609.34, m :1, km :1000, yd :0.9144, in: 0.0254};

let num = parseFloat(prompt("What is the distance?"));

let inUnit = prompt("What are the input units: <ft, mi, m, km, yd or in>?");

let outUnit = prompt("What are the output units: <ft, mi, m, km, yd or in>?");

function conversion(num, inUnit, outUnit) {
    return num * toMeters[inUnit]/toMeters[outUnit]}

alert(`${num} ${inUnit} equals ${conversion(num, inUnit, outUnit).toFixed(2)} ${outUnit}`)
