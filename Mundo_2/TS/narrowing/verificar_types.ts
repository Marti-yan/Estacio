let parametro:any

if(typeof parametro === "string"){}
if(typeof parametro === "number"){}
if(typeof parametro === "boolean"){}
if(typeof parametro === "bigint"){}
if(typeof parametro === "symbol"){}
if(typeof parametro === "undefined"){}
if(typeof parametro === "object"){}
if(typeof parametro === "function"){}


function testar_confianca(x: number, y?: number):number {
  return x + (y ?? 10);
}
let x1: number = testar_confianca(1, 9);
let x2: number = testar_confianca(1);
let x3: number = testar_confianca(1, undefined);
console.log(`Teste 1: ${x1}`);
console.log(`Teste 2: ${x2}`);
console.log(`Teste 3: ${x3}`);

