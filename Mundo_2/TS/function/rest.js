"use strict";
//----------------------------------------------
// Uso tradicional de uma função Rest
//----------------------------------------------
function saudar_pessoas(saudacao, ...nomes_pessoas) {
    return saudacao + " " + nomes_pessoas.join(", ") + "!";
}
let msg1 = saudar_pessoas("Bom dia!", "Alunos", "Alunas");
let msg2 = saudar_pessoas("Bom dia!", "Alunos", "Alunas", "Professoras", "Professores");
console.log(`Primeira saudação: ${msg1}`);
console.log(`Segunda saudação: ${msg2}`);
//----------------------------------------------
// Exemplo com arrow function
//----------------------------------------------
let saudar_pessoas_af = (saudacao, ...nomes_pessoas) => {
    return saudacao + " " + nomes_pessoas.join(", ") + "!";
};
let msg3 = saudar_pessoas_af("Bom dia!", "Alunos", "Alunas");
let msg4 = saudar_pessoas_af("Bom dia!", "Alunos", "Alunas", "Professoras", "Professores");
console.log(`\nPrimeira saudação: ${msg3}`);
console.log(`Segunda saudação: ${msg4}`);
