const texto='table football, foosball';

er = /[a-z]/;
result = texto.search(er);
if(texto.search(er) != -1) { //Retorna o index caso dê case com o alvo
console.log("Casou");
console.log(result); 
console.log(texto[result]);
} else {
console.log("Não casou");
}