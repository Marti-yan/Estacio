var alunos = []; //array vazio
var alunos = ['Alex', 'Anna', 'João']; // array de strings
var notas = [10.0, 9.5, 9.5]; // array de números decimais
var mistura = ['Um', 2, 3, 'Quatro']; //array de diversos tipos de dados

var alunos = new Array();  // MODO POO
var alunos = new Array('Alex', 'Anna', 'João');

console.log(alunos[0])
console.log(alunos)

////////////////////////////////
// adicionar ao array

alunos.push("Helena","Maria")  // adiciona o item na ultima posição
console.log(alunos)

alunos[alunos.length] = 'Yan';
console.log(alunos)

///////////////////////////////////////

alunos.splice(4,0,'Yuri') // 4 é o index onde sera inserido       0/1 indica se sera ou não excluido     'x' oq sera inserido 
console.log(alunos)

alunos.splice(1,1,'Thais') // 1 = excluir
console.log(alunos)

let removidos = alunos.splice(4,2,'Rebeca','Rafael') // 2 = ele exclui mas salva qual ele excluiu
console.log(alunos)
console.log(removidos)

////////////////////////////////////////////////////////////////

console.log(alunos.length)

delete alunos[2]
console.log(alunos, alunos.length)

////////////////////////////////////////////////////////////////
alunos.pop()    // remove o ultimo index
alunos.shift() //  remove o primeiro index [0]
console.log(alunos, alunos.length)


////////////////////////////////////////////////////////////////
var primos = [2,3,5,7,11,13,17];

primos.splice(3,2); //(x,y)   // exclui y numeros apartir do index[x]

console.log(primos);
