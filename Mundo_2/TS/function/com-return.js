"use strict";
function somar(x, y) {
    return x + y;
}
let t = 10;
let s = 20;
let soma = somar(t, s);
console.log(`A soma de ${t} com ${s} é: ${soma}`);
// ///////////////////////////////////////////////////////
function concatenar_texto(x, y) {
    return x + ", " + y;
}
let t1 = "primeiro";
let t2 = "segundo";
let texto_concat = concatenar_texto(t1, t2);
console.log(`A concatenação de ${t1} com ${t2} é: ${texto_concat}`);
