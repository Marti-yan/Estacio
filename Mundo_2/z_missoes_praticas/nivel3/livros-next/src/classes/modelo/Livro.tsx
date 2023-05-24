import React, {useState} from "react";


export interface LivroProps{
    codigo: number;
    codEditora: number;
    titulo: string;
    resumo: string;
    autores: string[];
}

class Livro extends React.Component<LivroProps> {
    constructor(props: LivroProps){
        super(props);
    }
    render(){
        let {codigo, codEditora, titulo, resumo, autores} = this.props;
        return(
            <>
                <div>
                    <h1>Livro</h1>
                    <p>codigo: {codigo}</p>
                    <p>Código da editora: {codEditora}</p>
                    <p>Titulo: {titulo}</p>
                    <p>Resumo: {resumo}</p>
                    <p>Autores: {autores}</p>
                </div>
            </>
        )
    }
}

export default Livro