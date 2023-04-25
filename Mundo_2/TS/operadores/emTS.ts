let a, b, valor: number;
a = 10;
b = 20;

valor = a+b; // adição de a com b
console.log("a + b: " + valor);
valor = a-b; // subtração de a com b
console.log("a - b: " + valor);
valor = a*b; // multiplicação de a com b
console.log("a * b: " + valor);
valor = a/b; // divisão de a com b
console.log("a / b: " + valor);
valor = a**2; // a elevado a 2
console.log("a**2 : " + valor);
valor = a%b; // resto da divisão inteira de a por b
console.log("a % b: " + valor);
valor = 5;
valor += a; // equivale a: valor = valor+a
console.log("valor += a : " + valor);
valor = 5;
valor -= a; // equivale a: valor = valor-a
console.log("valor -= a : " + valor);
valor = 5;
valor *= a; // equivale a: valor = valor*a
console.log("valor *= a : " + valor);
valor = 5;
valor /= a; // equivale a: valor = valor/a
console.log("valor /= a : " + valor);


let p1, p2, resultado: boolean;
p1 = true;
p2 = false;

resultado = p1 && p2;  // operador E
console.log("p1 &&  p2: " + resultado);
resultado = p1 || p2;  // operador OU
console.log("p1 ||  p2: " + resultado);
resultado = !p1;       // operador NEGAÇÃO
console.log("NOT p1: " + resultado);



let nota1, nota2, media: number; 
const peso1: number = 0.60; 
const peso2: number = 0.40; 
nota1 = 8.5;
nota2 = 6.5;
media = nota1*peso1 + nota2*peso2;
console.log("primeira nota: " + nota1 + " ,segunda nota: " + nota2);
console.log("média ponderada: " + media);
var res:boolean = ((media == 10)); 
console.log("(media == 10): ",res);
var res:boolean = ((media>9)&&(media<=9.5)); 
console.log("(media>9)&&(media<=9.5): ",res);
var res:boolean = ((media>=7)&&(media<9.5)); 
console.log("(media>=7)&&(media<9.5): ",res);
var res:boolean = ((media>=5)||(media<9)); 
console.log("(media>=5)||(media<9) ",res);








