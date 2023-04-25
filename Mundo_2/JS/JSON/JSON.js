const objs = [  // "JSON"
    {
        "nome": "Yan",
        "idade": 19,
        "trabalhando": true,
        "detalhes_profissao": {
            "profissao": "Programador",
            "empresa": "Martins-Tech"
        },
        "hobbies": [
            "programar",
            "jogar"
        ]
    },
    {
        "nome": "cleiton",
        "idade": 20,
        "trabalhando": false,
        "detalhes_profissao": {
            "profissao": null,
            "empresa": null
        },
        "hobbies": [
            "academiar",
            "jogar"
        ]
    }
]

console.log(objs)

// Transformar a variavel 'objs' em JSON valido
const jsondata = JSON.stringify(objs)
console.log(jsondata)


// Transformar o JSON para objeto
const jsonObj = JSON.parse(jsondata)
console.log(jsonObj)


// pegando os dados do JSON interno
const usuario = fetch("dados.json").then((response)=> {
    response.json().then((usuarios) => {
        console.log(usuarios)
    })
})


