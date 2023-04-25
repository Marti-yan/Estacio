
export class Pessoa {
    private nome: string = ''; // default
    protected ender: string = '';

    constructor(nome: string, ender: string) {
        this.set_Nome(nome);
        this.set_Ender(ender);
    }

    /////////  formas diferentes   ///////////////
    private set_Nome = (nome: string) => {
        this.nome = nome;
    }
    //
    private set_Ender(ender: string) {
        this.ender = ender;
    }
    //////////////////////////////////////////////

    public get_Nome = (): string => {
        return this.nome;
    }
    //
    public get_Ender = (): string =>{
        return this.ender;
    }
}

