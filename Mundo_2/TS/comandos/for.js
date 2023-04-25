"use strict";
let vetor2 = [7, 5, 10, 20, 30, 40, 2, 1, 1];
let maior2;
// forma 1: percorrer um vetor através dos índices dele
let n = vetor2.length;
maior2 = vetor2[0];
for (let i = 1; i < n; i++) {
    if (vetor2[i] > maior2) {
        maior2 = vetor2[i];
    }
}
console.log(maior2);
// forma 2: percorrer os elementos do vetor
maior2 = vetor2[0];
for (let valor of vetor2) {
    if (valor > maior2) {
        maior2 = valor;
    }
}
console.log(maior2);
