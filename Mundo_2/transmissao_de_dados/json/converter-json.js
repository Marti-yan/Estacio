//Cria um objeto Javacript
var objetoJS   = {agencia: "5678-9", tipo: "física", nome: "Maria José", numero: "222.222-22"};
console.log(objetoJS);
console.log("Objeto Original \n");


//Converte o objeto Javascript em texto JSON
var textoJson = JSON.stringify(objetoJS);
console.log(textoJson);
console.log("JSON \n");


// Converte de JSON para Objeto
var jsondata = JSON.parse(textoJson);
console.log(jsondata);
console.log("Objeto vindo do JSON");

// salvando no navegador
localStorage.setItem("stringJSON", textoJson);  


// variavel pra recuperar oq esta salvo no navegador
var JsonLS = localStorage.getItem("stringJSON");
console.log(JsonLS);

// transforma a variavel que veio do navegador de str pra OBJ
var LSobj = JSON.parse(JsonLS);
console.log(LSobj);