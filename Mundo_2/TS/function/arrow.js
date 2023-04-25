"use strict";
let soma1 = (x, y) => {
    return x + y;
};
let soma2 = (x, y) => x + y;
let c = 10;
let d = 20;
console.log(`Teste 01: a soma de ${c} com ${d} é: ${soma1(c, d)}`);
console.log(`Teste 02: a soma de ${c} com ${d} é: ${soma2(c, d)}`);
