import { Pessoa } from "./encapsulamento";
import { PessoaFisica, PessoaJuridica } from "./heranca";

const pessoa2 = new Pessoa('Yan', 'arara azul')
const pessoa3 = new PessoaFisica('Yan 2N', 'arara','123.456.987-10')
const pessoa4 = new PessoaJuridica('Martins Tech','RJ','961.0001/07')

console.log(pessoa2.get_Nome())
console.log(pessoa3.get_Dados())
console.log(pessoa4.get_Dados())

