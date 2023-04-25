class Estudante<T,U>{
    private id: T|undefined;
    private name: U|undefined;
    public set_valor(id: T,name: U):void {
        this.id = id;
        this.name = name;
    }
    public exibir_dados():void{
        console.log(`Id: ${this.id}, Nome: ${this.name}`)
    }
}

let estudante_01 = new Estudante<number,string>();
estudante_01.set_valor(1301,"Yan");
estudante_01.exibir_dados();

let estudante_02 = new Estudante<number,string>();
estudante_02.set_valor(2004,"Martins")
estudante_02.exibir_dados();