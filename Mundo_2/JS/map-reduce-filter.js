// conteudo fora das aulas da faculdade!

const precos = [
    "Crédito",
    "R$ 200",
    "R$ 400",
    "Contas a pagar",
    "R$ 300",
    "R$ 400",
    "Meus dados"
];

// FILTER
// const precosFiltro = precos.filter(function(preco){
//     console.log(preco);
//     if(preco.includes("R$")){
//         return true;
//     }
// })

// FILTER simplificado
const precosFiltro = precos.filter(preco => preco.includes("R$"));
console.log(precosFiltro)

//   MAP
// const precoNumeros = precosFiltro.map(function(preco){
//     console.log(preco)
//     return +preco.replace("R$ ","");  // esse + na frente tranforma para NUMBER || Number(...)
// })

// MAP simplificado
const precoNumeros = precosFiltro.map(preco =>  +preco.replace("R$ ",""));  // esse + na frente tranforma para NUMBER || Number(...)
console.log(precoNumeros)

// REDUCE // sempre tras um valor unico no final
// const total = precoNumeros.reduce(function(acumulador, item){
//     return acumulador+item;
// },1000) // serve pra adicionar este valor no total

// REDUCE simplificado
const total = precoNumeros.reduce((acumulador, item) => acumulador+item) // serve pra adicionar este valor no total
console.log(total)

const editoras = [
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

const nomes = editoras.map(editora => editora.nome);

console.log(nomes);

const jsonData = [
    {
      codEditora: 1,
      nome: "yan"
    },
    {
      codEditora: 2,
      nome: "Martins"
    },
    {
      codEditora: 3,
      nome: "D'Tech"
    }
  ];
  
  const filtro = 2;
  const resultadoFiltro = jsonData
    .filter(item => item.codEditora === filtro)
    .map(item => item.nome);
  
  console.log(resultadoFiltro);
  