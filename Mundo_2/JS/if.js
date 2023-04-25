var a = 10;
var b = 3;

console.log ("if com uma única condição:");
if (a > b){
    console.log("a é maior que b");
}
if (a == b){
   console.log("a é igual a b"); 
}
if (a < b){
    console.log("a é menor que b");
}
if (b < a){
	console.log("b é menor que a");
}

console.log()
console.log("///////////////////////////")
console.log()

var c = 5;
var d = -1;

console.log("if com duas condições, onde ambas precisam ser verdadeiras:");
if (c > d && d > 0){
    console.log("c é maior que d E d é um número positivo");
}
if (c > d && d <= 0){
    console.log("c é maior que d E d não é um número positivo");
}

console.log()
console.log("///////////////////////////")
console.log()

console.log("if com duas condições, onde pelo menos uma precisa ser verdadeira:");  
if (c < d || d > 0){
    console.log("c é menor que d OU d é um número positivo");
}
if (c < d || d <= 0){
    console.log("c é menor que d OU d não é um número positivo");
}

console.log()
console.log("///////////////////////////")
console.log()

var e = 5;
var f = -1;
var g = false; // valores possíveis -> True, False

console.log("if com mais de duas condições e combinação de && e ||:");
if ((e > f && f > 0) || (e > f && f <= 0)){
    console.log("e é maior que f E f é um número positivo");
    console.log("OU");
    console.log("e é maior que f E f não é um número positivo");
}

console.log()
console.log("///////////////////////////")
console.log()

console.log("if com condição não verdadeira:");
if (!g){
    console.log("g tem valor false");
}