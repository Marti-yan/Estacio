import React from "react";
import Editora, {EditoraProps} from '../modelo/Editora'

const editorass: EditoraProps[] = [
    {
        codEditora:1,
        nome: "yan"
    },
    {
        codEditora:2,
        nome: "Martins"
    },
    {
        codEditora:3,
        nome:"D'Tech"
    }
]


class ControleEditora extends React.Component{
    constructor(editoras: EditoraProps[]){
        super(editorass)
    }

    getNomeEditora = (codeditora:number):string[] =>{
        // alert(editorass[codEditora].nome);
        const editora = editorass.filter(item => item.codEditora == codeditora).map(item => item.nome);
        return editora
    }
    getEditoras = ():string[] =>{
        const nomes = editorass.map(editora => editora.nome)
        return nomes
    }
}

export default ControleEditora