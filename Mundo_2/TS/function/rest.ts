//----------------------------------------------
// Uso tradicional de uma função Rest
//----------------------------------------------
function saudar_pessoas(saudacao: string, ...nomes_pessoas: string[]) {
    return saudacao + " " + nomes_pessoas.join(", ") + "!";
}

let msg1: string = saudar_pessoas("Bom dia!", "Alunos", "Alunas"); 
let msg2: string = saudar_pessoas("Bom dia!", "Alunos", "Alunas", "Professoras", "Professores");
console.log(`Primeira saudação: ${msg1}`);
console.log(`Segunda saudação: ${msg2}`);


//----------------------------------------------
// Exemplo com arrow function
//----------------------------------------------

let saudar_pessoas_af = (saudacao: string, ...nomes_pessoas: string[]) => {
    return saudacao + " " + nomes_pessoas.join(", ") + "!";
}

let msg3: string = saudar_pessoas_af("Bom dia!", "Alunos", "Alunas");
let msg4: string = saudar_pessoas_af("Bom dia!", "Alunos", "Alunas" , "Professoras", "Professores")

console.log(`\nPrimeira saudação: ${msg3}`);
console.log(`Segunda saudação: ${msg4}`);