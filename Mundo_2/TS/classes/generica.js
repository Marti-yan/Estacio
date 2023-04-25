"use strict";
class Estudante {
    set_valor(id, name) {
        this.id = id;
        this.name = name;
    }
    exibir_dados() {
        console.log(`Id: ${this.id}, Nome: ${this.name}`);
    }
}
let estudante_01 = new Estudante();
estudante_01.set_valor(1301, "Yan");
estudante_01.exibir_dados();
let estudante_02 = new Estudante();
estudante_02.set_valor(2004, "Martins");
estudante_02.exibir_dados();
