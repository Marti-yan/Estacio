var texto = "TestanDo";//Texto alvo
var er = /[a-z]/g; //Regex - letras minúsculas  // g- global
let result = texto.match(er);//Função string para pesquisar o regex 
console.log(result); //['e', index: 1, input: 'Testando', groups: undefined]

er = new RegExp('[A-Z]', 'g'); //Regex - letras maiúsculas 
result = texto.match(er);
console.log(result); //['T', index: 0, input: 'Testando', groups: undefined]

