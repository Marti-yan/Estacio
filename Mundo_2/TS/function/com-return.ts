function somar(x: number, y: number): number {
    return x + y;
}

let t: number = 10;
let s: number = 20;

let soma = somar(t, s);
console.log(`A soma de ${t} com ${s} é: ${soma}`)

// ///////////////////////////////////////////////////////

function concatenar_texto(x: string, y: string): string {
    return x + ", " + y;
}

let t1: string = "primeiro";
let t2: string = "segundo";
let texto_concat = concatenar_texto(t1, t2);
console.log(`A concatenação de ${t1} com ${t2} é: ${texto_concat}`);