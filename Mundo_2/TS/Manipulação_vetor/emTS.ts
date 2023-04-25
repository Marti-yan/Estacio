// vetor de numeros
let vetorNumerosTS: number[] = [7,5,2,1,1];

// vetor de strings
let vetorStringTs: string[] = ['javascript','typeScript','web']

console.log("Resultados com TypeScript");            
console.log("x[0]= " + vetorNumerosTS[0]);          
console.log("x[1]= " + vetorNumerosTS[1]);          
console.log("x[2]= " + vetorNumerosTS[2]);  

//Adiciona um elemento a um vetor
vetorNumerosTS.push(3);
console.log("x= " + vetorNumerosTS);     

//adicionar um elemento no início do vetor
vetorNumerosTS.unshift(9); 
console.log("x= " + vetorNumerosTS);   

//modificar um elemento do vetor
vetorNumerosTS[0] = 1976; 
console.log("x= " + vetorNumerosTS); 

// remove o último elemento do vetor
let elementoRemovidoTS = vetorNumerosTS.pop();
//imprimir o elemento
console.log("elemento removido:" + elementoRemovidoTS);
console.log(vetorNumerosTS); 

// remover o primeiro elemento
elementoRemovidoTS = vetorNumerosTS.shift();
console.log("elemento removido: " + elementoRemovidoTS); 
console.log(vetorNumerosTS); 

// Retorna o comprimento do vetor
console.log("o comprimento do vetor é: "+vetorNumerosTS.length); 

// ordenação dos elementos
vetorNumerosTS.sort();
console.log("vetor ordenado: " + vetorNumerosTS); 

//encontrar o índice de um elemento dentro do vetor
const posicaoTS = vetorNumerosTS.indexOf(7);
console.log("Posição do elemento dentro do vetor: " + posicaoTS);