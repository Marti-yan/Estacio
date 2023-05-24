import React from "react";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import "./app2.css"
import Editora from "./modelo/Editora";
import ControleEditora from "./controle/ControleEditora";
import Livro from "./modelo/Livro";
import LivroLista from "./livro/LivroLista";
import LD from "./livro/LivroDados";

// const teste: React.FC = () => {
//   const CE = new ControleEditora();
//   const getEdit = () => {
//     CE.getEditoras()
//   }
// }
function App() {
  return (
    <>
      <div>
        <BrowserRouter>
          <nav className="navbar bg-dark">
            <button className="btn btn-outline-success me-2" type="button">
              <Link to="/"> Catalogo </Link>
            </button>
            <button className="btn btn-outline-success me-2" type="button">
              <Link to="/dados"> Novo</Link>
            </button>
          </nav>

          <Routes>
            <Route path="/" element={<LivroLista />} />
            <Route path="/dados" element={<LD />} />
          </Routes>
        </BrowserRouter>
      </div>
    </>
  );
}

export default App;
