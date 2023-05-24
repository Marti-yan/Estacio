import React, {useState} from "react";
import Livro, { LivroProps } from "../modelo/Livro";
import ControleEditora from "./ControleEditora";

const livros: LivroProps[] = [
  {
    codigo: 1,
    codEditora: 123,
    titulo: "Livro 1",
    resumo: "Resumo do Livro 1",
    autores: ["Autor 1", "Autor 2"],
  },
  {
    codigo: 2,
    codEditora: 456,
    titulo: "Livro 2",
    resumo: "Resumo do Livro 2",
    autores: ["Autor 3", "Autor 4"],
  },
  {
    codigo: 3,
    codEditora: 789,
    titulo: "Livro 3",
    resumo: "Resumo do Livro 3",
    autores: ["Autor 5", "Autor 6"],
  },
];

class ControleLivro extends React.Component {
  constructor(livro: LivroProps[]) {
    super(livro);
    // const [livros, setLivros] = useState<LivroProps[]>([])
  }

   Obter_Livros = ():any => {

    return (
      <>
       <tr>
        <td>{livros.map(livro => livro.titulo)}</td>
        <td>{livros.map(livro => livro.resumo)}</td>
        {/* <td>{livros.map(livro => livro.codEditora).map(codEditora => ControleEditora.getNomeEditora(Livro.codEditora))}</td> */}
        <td>{livros.map(livro => livro.resumo)}</td>
        <td>{livros.map(livro => <ul><li>{livro.autores}</li></ul>)}</td>
       </tr>
      </>
    )
  };

  Incluir_Livros = (livro: LivroProps[]):void =>  {
    const novocod = livros.length + 1;
    livros.push(...livros, livro[novocod]);
  };
  Excluir_Livros = (codigo: number):any => {
    return livros.filter(l => l.codigo !== codigo)
  };
}

export default ControleLivro
