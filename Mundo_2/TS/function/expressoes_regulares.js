"use strict";
function checar_padrao(par_padrao, par_texto) {
    if (par_padrao.test(par_texto)) {
        return "Foi detectado o padrão dentro do texto";
    }
    return "Não foi encontrado o padrão dentro do texto";
}
const texto_teste = "O objetivo desse texto é realizar testes, By Yan Martins";
const texto_teste2 = "O objetivo desse texto é realizar testes, 2023-04-07";
const padrao_regex = /Yan/;
const padrao_regex2 = /[0-9]{4}[-][0-9]{2}[-][0-9]{2}/;
let res_teste = checar_padrao(padrao_regex, texto_teste);
let res_teste2 = checar_padrao(padrao_regex2, texto_teste2);
console.log(`O resultado da execução do regex foi: ${res_teste} \n O resultado da execução do regex2 foi: ${res_teste2}`);
// /////////////////////////////////////////////////////////////////
function checar_todas_palavras(par_padrao, par_texto) {
    let total = 0;
    for (let i of par_texto) {
        if (par_padrao.test(i)) {
            total++;
        }
    }
    return total;
}
// ////////////////////////////////////////////////////////////////////////////////
const vetor_texto = ["12345-657", "82345-67", "123aa-67", "92445-467"];
const p_regex = /\d{5}-\d{3}/; //   \d == [0-9]   e pelo visto não precisa necesariamente dos '[]' no '-' | '[-]' == '-'
let r_teste = checar_todas_palavras(p_regex, vetor_texto);
let tmn = vetor_texto.length;
console.log(`Das ${tmn} palavras, o total que satisfaz o padrão ${p_regex} é de: ${r_teste}`);
// ////////////////////////////////////////////////////////////////////////////////
