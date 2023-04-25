"use strict";
function fatorial(n) {
    if ((n == 0) || (n == 1)) {
        return 1;
    }
    return n * fatorial(n - 1);
}
let numeroF = 5;
let res_fat = fatorial(numeroF);
console.log(`O fatorial do numero ${numeroF} é: ${res_fat}`);
