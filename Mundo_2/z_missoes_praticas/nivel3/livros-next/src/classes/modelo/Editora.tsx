import React, { useState } from "react";

class Editora extends React.Component<EditoraProps> {
  constructor(props: EditoraProps) {
    super(props);
  }
  render() {
    let {codEditora, nome} = this.props;
    return (
      <>
        <div>
          <h1>Editora</h1>
          <p>Código: {/*this.props.*/codEditora}</p>
          <p>Nome: {/*this.props.*/nome}</p>
        </div>
      </>
    );
  }
}

export interface EditoraProps {
  codEditora: number;
  nome: string;
}

export default Editora;
