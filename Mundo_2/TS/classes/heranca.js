"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.PessoaJuridica = exports.PessoaFisica = void 0;
const encapsulamento_1 = require("./encapsulamento");
class PessoaFisica extends encapsulamento_1.Pessoa {
    constructor(nome, ender = '', cpf) {
        super(nome, ender);
        this.cpf = '';
        this.set_Cpf = (cpf) => {
            this.cpf = cpf;
        };
        this.get_Cpf = () => {
            return this.cpf;
        };
        this.get_Dados = () => {
            console.log(`Dados da pessoa física: nome = ${this.get_Nome()}, 
        endereço = ${this.get_Ender()}, 
        cpf = ${this.get_Cpf()}`);
        };
        this.set_Cpf(cpf);
    }
}
exports.PessoaFisica = PessoaFisica;
class PessoaJuridica extends encapsulamento_1.Pessoa {
    constructor(nome, ender = '', cnpj = '') {
        super(nome, ender);
        this.cnpj = '';
        this.get_Cnpj = () => {
            return this.cnpj;
        };
        this.get_Dados = () => {
            console.log(`Dados da pessoa juridica: \n -Nome = ${this.get_Nome()} \n -Endereço = ${this.get_Ender()} \n -CNPJ = ${this.get_Cnpj()}`);
        };
        this.set_Cnpj(cnpj);
    }
    // opção melhor 
    // private set_Cnpj = (cnpj: string) => {
    //     this.cnpj = cnpj;
    // }
    set_Cnpj(cnpj) {
        this.cnpj = cnpj;
    }
}
exports.PessoaJuridica = PessoaJuridica;
