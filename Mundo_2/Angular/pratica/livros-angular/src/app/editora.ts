import { Component, Input } from '@angular/core';

export interface EditoraProps {
  codEditora: number;
  nome: string;
}

@Component({
  selector: 'app-editora',
  template: `
    <div>
      <h1>Editora</h1>
      <p>Código: {{ codEditora }}</p>
      <p>Nome: {{ nome }}</p>
    </div>
  `,
})
export class EditoraComponent {
    codEditora: number = 0;
    nome: string = '';
}