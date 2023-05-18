texto= "Comando 1;Ação 2;Tarefa 3;Resultado 4";
regex = /;/;
result = texto.split(regex);
console.log(result); // [ 'Comando 1', 'Ação 2', 'Tarefa 3', 'Resultado 4' ]

result = texto.split(regex,2);
console.log(result); // [ 'Comando 1', 'Ação 2' ]