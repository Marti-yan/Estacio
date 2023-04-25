"use strict";
// Narrowing com if (refinamento)
function testar_type(par_valor) {
    if (typeof par_valor === 'number') {
        return par_valor;
    }
    if (typeof par_valor === 'string') {
        return par_valor.length;
    }
    throw new Error('O parametro possui um tipo diferente dos quais são suportados! ' + par_valor);
}
let t_msg = testar_type("txt teste");
console.log(`O resultado da execução da função é: ${t_msg}`);
// ///////////////////////////////////////////////////////////////////
function testar_type2(par_valor2) {
    switch (typeof par_valor2) {
        case 'number':
            return 'number' + par_valor2;
        case 'string':
            return 'string' + par_valor2;
        default:
            throw new Error('O parâmetro possui um tipo que não é suportado');
    }
}
let msg = testar_type2("isto é um teste");
console.log(`O resultado da execução da função é: ${msg}`);
