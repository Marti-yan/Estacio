
// vetor de números
let vetorNumerosJS = [7,5,2,1,1];
// vetor de strings
let vetorStringJS = [ 'javascript', 'typescript', 'web'];


console.log("Resultados com JavaScript");            
console.log("x[0]= " + vetorNumerosJS[0]);          
console.log("x[1]= " + vetorNumerosJS[1]);          
console.log("x[2]= " + vetorNumerosJS[2]);    

//Adiciona um elemento a um vetor
vetorNumerosJS.push(3);
console.log("x= " + vetorNumerosJS);   

//adicionar um elemento no início do vetor
vetorNumerosJS.unshift(9); 
console.log("x= " + vetorNumerosJS);       

//modificar um elemento do vetor
vetorNumerosJS[0] = 1976; 
console.log("x= " + vetorNumerosJS);    

// remove o último elemento do vetor
let elementoRemovidoJS = vetorNumerosJS.pop();
//imprimir o elemento
console.log("elemento removido:" + elementoRemovidoJS);
console.log(vetorNumerosJS); 

// remover o primeiro elemento
elementoRemovidoJS = vetorNumerosJS.shift();
console.log("elemento removido: " + elementoRemovidoJS); 
console.log(vetorNumerosJS); 

// Retorna o comprimento do vetor
console.log("o comprimento do vetor é: "+vetorNumerosJS.length); 

// ordenação dos elementos
vetorNumerosJS.sort();
console.log("vetor ordenado: " + vetorNumerosJS); 

//encontrar o índice de um elemento dentro do vetor
const posicaoJS = vetorNumerosJS.indexOf(7);
console.log("Posição do elemento dentro do vetor: " + posicaoJS); 