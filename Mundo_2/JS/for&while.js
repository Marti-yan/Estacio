var contador
for (contador = 0; contador < 10; contador++){
    console.log(contador)
}

console.log("\n //////////////////////// \n")


var frutas = ['Laranja', 'Uva', 'Pera'];

// for normal
for(var i = 0; i < frutas.length; i++){
	console.log(`Nome da Fruta contida no Array: ${frutas[i]}`)
}

console.log()

// for in
for ( let index_fruta in frutas){
	console.log(`Index da Fruta contida no Array: ${index_fruta}`)
}

console.log()

// for of
for (let fruta2 of frutas){
    console.log(`Nome da Fruta contida no Array: ${fruta2}`)
}


console.log("\n //////////////////////// \n")

var contador2 = 0;
while (contador2 < 10){
    console.log(contador2)
    contador2++;
}

console.log("\n //////////////////////// \n")


//“do/while” A condição é testada no final.
// Logo pelo menos uma vez a instrução (ou as instruções) do laço “do/while” será, obrigatoriamente, executada.
var contador3 = 0;
do{
    contador3 += 1;  // primeiro ele executa o codigo (nesse caso soma)
    console.log(contador3) // dps ele mostra ja dps de feito
}while(contador3 < 10)  // e so depois ele verifica (por isso ele vai do 1 ao 10)