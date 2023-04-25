let numero = []

let n1 = Number(prompt("Informe um numero inteiro e positivo: "));
let n2 = Number(prompt("Informe outro numero inteiro e positivo: "));

if (n1 >= 0 && n2 >= 0 && Number.isInteger(n1) && Number.isInteger(n2)) {
    numero.push(n1,n2);
} else {
    alert(" algum dos numeros não eram inteiros ou positivos")
}
const divisao = numero.reduce((n1,n2) => n1 / n2)
alert(`O resultado da divisão é: ${divisao}`)