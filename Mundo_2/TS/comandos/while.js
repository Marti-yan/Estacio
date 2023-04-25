"use strict";
let vetor = [7, 5, 40, 20, 70, 50, 2, 1, 1];
let maior;
let i;
let tam = vetor.length;
//forma 1: o teste é realizado antes de entrar no bloco de comandos
i = 0;
maior = vetor[0];
while (i < tam) {
    if (vetor[i] > maior) {
        maior = vetor[i];
    }
    i++;
}
console.log("Forma 01: O maior elemento do vetor é:" + maior);
//forma 2: teste é realizado depois de entrar no bloco de comandos
i = 0;
tam = vetor.length;
maior = vetor[0];
do {
    if (vetor[i] > maior) {
        maior = vetor[i];
    }
    i++;
} while (i < tam);
console.log("Forma 02: O maior elemento do vetor é:" + maior);
