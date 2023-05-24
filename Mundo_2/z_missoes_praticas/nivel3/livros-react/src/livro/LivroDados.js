import React, { useEffect, useState } from 'react';
import ControleEditora from '../controle/ControleEditora';

const LivroDados = () => {
  const [opcoes, setOpcoes] = useState([]);

  useEffect(() => {
    const controleEditora = new ControleEditora();
    const editoras = controleEditora.getEditoras();

    const opcoesMapeadas = editoras.map((editora) => ({
      value: editora.codEditora,
      text: editora.nome,
    }));

    setOpcoes(opcoesMapeadas);
  }, []);

  return (
    <>
    <div>
      {/* Acesse as informações do estado opcoes aqui */}
      {opcoes.map((opcao) => (
        <div key={opcao.value}>
          <span>{opcao.text}</span>
        </div>
      ))}
      <h1>Dados do Livro</h1>
      <form className="mb-3">
        <label className="form-label">Título</label> <br />
        <input type="text" className="form-control" /> <br />
        <label className="form-label" >Resumo</label> <br />
        <textarea className="form-control"  /> <br />
        <label className="form-label" >Editora</label><br />
        <select className="form-control" >
        {opcoes.map((opcao) => (
        <option key={opcao.value}>
          {opcao.text}
        </option>
      ))}
        </select><br />
        <label className="form-label" >Autores (1 por linha)</label> <br />
        <textarea className="form-control"  /> <br />

        <button type="submit" className="btn btn-primary">Salvar Dados</button>
      </form>
    </div>
    </>
  );
};

export default LivroDados;
