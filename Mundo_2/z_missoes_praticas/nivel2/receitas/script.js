const receitass = [
    {
        titulo: "Bolo de cenoura",
        imagem: "./src/bolo_cenoura.png",
        preparo: "1. Preaqueça o forno a 180 °C. 2. Em um liquidificador, bata a cenoura, os ovos e o óleo até formar um creme. 3. Em uma tigela, misture a farinha, o açúcar e o fermento. 4. Adicione a mistura do liquidificador à tigela e mexa até obter uma massa homogênea. 5. Despeje a massa em uma forma untada e enfarinhada. 6. Leve ao forno por cerca de 40 minutos.",
        ingredientes: [
            "3 cenouras",
            "3 ovos",
            "1 xícara de óleo",
            "2 xícaras de açúcar",
            "2 xícaras de farinha de trigo",
            "1 colher de sopa de fermento em pó"
        ]
    },
    {
        titulo: "Lasanha à bolonhesa",
        imagem: "./src/lasanha.png",
        preparo: "1. Em uma panela, refogue a carne moída com cebola e alho. 2. Adicione o molho de tomate e tempere com sal e pimenta a gosto. 3. Em outra panela, prepare o molho branco, derretendo a manteiga e adicionando a farinha. 4. Adicione o leite aos poucos, mexendo sempre, até engrossar. 5. Em um refratário, faça camadas alternadas de molho de carne, massa de lasanha e molho branco. 6. Finalize com queijo ralado. 7. Leve ao forno preaquecido a 200 °C por cerca de 30 minutos.",
        ingredientes: [
            "500g de carne moída",
            "1 cebola picada",
            "2 dentes de alho picados",
            "1 lata de molho de tomate",
            "Sal e pimenta a gosto",
            "2 colheres de sopa de manteiga",
            "2 colheres de sopa de farinha de trigo",
            "500ml de leite",
            "Massa de lasanha",
            "Queijo ralado"
        ]
    },
    {
        "titulo": "Frango Xadrez",
        "imagem": "./src/frango.png",
        "preparo": "1. Em uma tigela, tempere o frango com o shoyu, o saquê e o amido de milho. 2. Em uma frigideira, aqueça o óleo e frite o frango até dourar. Reserve. 3. Na mesma frigideira, refogue a cebola, o pimentão e a cenoura. 4. Adicione o molho de tomate e o açúcar e mexa bem. 5. Junte o frango reservado e deixe cozinhar por mais alguns minutos. 6. Sirva com arroz branco.",
        "ingredientes": [
            "500g de peito de frango cortado em cubos",
            "2 colheres de sopa de shoyu",
            "2 colheres de sopa de saquê",
            "2 colheres de sopa de amido de milho",
            "1 cebola cortada em cubos",
            "1 pimentão verde cortado em cubos",
            "1 cenoura cortada em cubos",
            "1/2 xícara de molho de tomate",
            "1 colher de sopa de açúcar",
            "Óleo para fritar"
        ]
    }
];
let listas = [];




function preencherCatalogo() {
    let dados = getCard(receitass)
    let catalogo = document.getElementById('pnlCatalogo');
    catalogo.innerHTML = dados
}

const getListaIngredientes = (receita) => {
    // listas = [];
    // for (let receita of receitas) {
    //   let lista = '<ul>';
    //   for (let ingrediente of receita.ingredientes) {
    //     lista += `<li>${ingrediente}</li>`;
    //   }
    //   lista += '</ul>';
    //   listas.push(lista);
    // }
    // return listas;
    
    // const ingredientes = receitas.map(objeto => {
        // return objeto.ingredientes;
    // });
    // console.log(ingredientes)
    // for (const receita in ingredientes) {
    //     let texto = ''
    //     let total = [];
    //     for (const item of ingredientes[receita]) {
    //         let itens = `<li>${item}</li>`;
    //         total.push(itens);
    //     }
    //     texto += `<ul> ${total.reduce((accum, item) => accum + item)} </ul>`
    //     listas.push(texto)
    // }

    let lista = []
    let ingredientes = receita.ingredientes
    const ingrediente = ingredientes.map(item => {
        lista.push(`<li>${item}</li>`)
    })
    let texto_UL = `<ul> ${lista.reduce((accum, lista) => accum + lista)} </ul>`
    return texto_UL;

};
// console.log(listas)
let getCard = (receitas) => {
//     let cards = []
//     for (const key in receitas) {
//         let card = `
//             <div class="card" style="width: 250px;">
//                 <img src="${receitas[key].imagem}" class="card-img-top" >
//                 <div class="card-body">
//                     <p class="card-title"> ${receitas[key].titulo} </p>
//                     <div class="card-text">
//                         ${getListaIngredientes(receitass[key])}
//                         <hr>
//                         <span> ${receitas[key].preparo} </span>
//                     </div>
//                 </div>
//             </div>  `
//         cards.push(card)
//     }
//     return cards
return Object.keys(receitas).map(key => {
    // console.log(key)
    return `
      <div class="card" style="width: 250px;">
        <img src="${receitas[key].imagem}" class="card-img-top" >
        <div class="card-body">
          <p class="card-title"> ${receitas[key].titulo} </p>
          <div class="card-text">
            ${getListaIngredientes(receitas[key])}
            <hr>
            <span> ${receitas[key].preparo} </span>
          </div>
        </div>
      </div>
    `
  }).reduce((prev, curr) => prev + curr, '')


}
