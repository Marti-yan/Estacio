import React, { useEffect, useState } from 'react';
import ControleEditora from '../controle/ControleEditora';
import ControleLivro from '../controle/ControleLivros';

const LinhaLivro = ({ livro, excluir }) => {
    const [nomeEditora, setNomeEditora] = useState('');
  
    useEffect(() => {
      const getNomeEditora = async () => {
        const nome = await ControleEditora.getNomeEditora(livro.codEditora);
        setNomeEditora(nome);
      };
  
      getNomeEditora();
    }, [livro.codEditora]);
  
    return (
      <tr>
        <td>
          <button onClick={() => excluir(livro.codigo)}>Excluir</button>
        </td>
        <td>{livro.codigo}</td>
        <td>{nomeEditora}</td>
        <td>{livro.titulo}</td>
        <td>{livro.resumo}</td>
        <td>
          <ul>
            {livro.autores.map((autor, index) => (
              <li key={index}>{autor}</li>
            ))}
          </ul>
        </td>
      </tr>
    );
  };
  
  const LivroLista = () => {
    const [livros, setLivros] = useState([]);
    const [carregado, setCarregado] = useState(false);
  
    const controleLivro = new ControleLivro();
    const controleEditora = new ControleEditora();
  
    useEffect(() => {
      const carregarLivros = async () => {
        const livros = await controleLivro.obterLivros();
        setLivros(livros);
        setCarregado(true);
      };
  
      carregarLivros();
    }, []);
  
    const excluir = codigo => {
      controleLivro.excluir(codigo);
      setCarregado(false);
    };
  
    return (
      <main>
        <br />
        <table className="table table-striped">
          <thead>
            <tr className="table-dark">
              <th>Título</th>
              <th>Resumo</th>
              <th>Editora</th>
              <th>Autores</th>
            </tr>
          </thead>
          <tbody>
            {livros.map(livro => (
              <LinhaLivro key={livro.codigo} livro={livro} excluir={excluir} />
            ))}
          </tbody>
        </table>
      </main>
    );
  };
  
  export default LivroLista;


