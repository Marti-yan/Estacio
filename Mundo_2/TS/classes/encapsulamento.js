"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Pessoa = void 0;
class Pessoa {
    constructor(nome, ender) {
        this.nome = ''; // default
        this.ender = '';
        /////////  formas diferentes   ///////////////
        this.set_Nome = (nome) => {
            this.nome = nome;
        };
        //////////////////////////////////////////////
        this.get_Nome = () => {
            return this.nome;
        };
        //
        this.get_Ender = () => {
            return this.ender;
        };
        this.set_Nome(nome);
        this.set_Ender(ender);
    }
    //
    set_Ender(ender) {
        this.ender = ender;
    }
}
exports.Pessoa = Pessoa;
