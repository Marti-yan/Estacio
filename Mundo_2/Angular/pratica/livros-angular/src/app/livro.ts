import { Component, Input } from '@angular/core';

export interface LivroProps {
  codigo: number;
  codEditora: number;
  titulo: string;
  resumo: string;
  autores: string[];
}

@Component({
  selector: 'app-livro',
  template: `
    <div>
      <h1>Livro</h1>
      <p>codigo: {{ codigo }}</p>
      <p>Código da editora: {{ codEditora }}</p>
      <p>Titulo: {{ titulo }}</p>
      <p>Resumo: {{ resumo }}</p>
      <p>Autores: {{ autores.join(', ') }}</p>
    </div>
  `,
})
export class LivroComponent {
  codigo: number = 0;
  codEditora: number = 0;
  titulo: string = '';
  resumo: string = '';
  autores: string[] = [];
}