import { Pessoa } from "./encapsulamento";

export class PessoaFisica extends Pessoa {
    private cpf: string = '';

    constructor(nome: string, ender: string = '', cpf: string) {
        super(nome, ender);
        this.set_Cpf(cpf);
    }
    private set_Cpf = (cpf: string) => {
        this.cpf = cpf;
    }
    public get_Cpf = (): string => {
        return this.cpf;
    }
    public get_Dados = (): void => {
        console.log(`Dados da pessoa física: nome = ${this.get_Nome()}, 
        endereço = ${this.get_Ender()}, 
        cpf = ${this.get_Cpf()}`);
    }

}

export class PessoaJuridica extends Pessoa {
    private cnpj: string = '';
    constructor(nome: string, ender: string = '', cnpj: string = '') {
        super(nome,ender);
        this.set_Cnpj(cnpj);
    }

    // opção melhor 
    // private set_Cnpj = (cnpj: string) => {
    //     this.cnpj = cnpj;
    // }
    private set_Cnpj(cnpj: string): void {
        this.cnpj = cnpj;
    }

    public get_Cnpj = ():string => {
        return this.cnpj;
    }

    public get_Dados = ():void => {
        console.log(`Dados da pessoa juridica: \n -Nome = ${this.get_Nome()} \n -Endereço = ${this.get_Ender()} \n -CNPJ = ${this.get_Cnpj()}`)
    }


}

