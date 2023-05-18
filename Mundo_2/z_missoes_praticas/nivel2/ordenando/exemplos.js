const input = document.getElementById('valor');
const lista = document.getElementById('valores');
let node = ''
let Vnode = ''
let lista2 = [];

input.addEventListener('keyup', function (e) {
    if (e.keyCode == 13) { // codigo da tecla enter
        add()
    }
});

function add() {
    node = document.createElement('li')

    if (input.value != '') {
        Vnode = document.createTextNode(input.value)
        node.appendChild(Vnode)
        lista.appendChild(node)
        lista2.push(input.value)
    }

    input.value = ''
}

function ordenar() {
    lista2 = []
    let itens = lista.children;

    for (item of itens) {
        lista2.push(item.textContent)
        lista2 = lista2.map(str => parseInt(str))
    }

    let operacoes = document.getElementById('operacoes')
    const index = operacoes.selectedIndex;

    if (index == 0) {
        bubble_sort(lista2)
    } else if (index == 1) {
        selection_sort(lista2)
    } else if (index == 2) {
        quick_sort(lista2, 0, lista2.length - 1)
        alterarLista(lista2)
    }

}

function misturar() {
    lista2 = []
    let valores = document.getElementById('valores')
    let itens = valores.children;
    for (item of itens) {
        lista2.push(item.textContent)
        lista2 = lista2.map(str => parseInt(str))
    }

    shuffle(lista2, lista2.length)
    // return arr.sort((a, b) => Math.random() - 0.5)
}

let alterarLista = (arr) => {
    lista.innerHTML = ''
    for (item of arr) {
        lista.innerHTML += '<li>' + item + '</li>'
    }
}

//////////////////////////////////////////////////////////////////////////
// const array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

let shuffle = (arr, x) => {
    for (let i = 0; i < x; i++) {
        let n1 = Math.floor(Math.random() * arr.length);
        let n2 = Math.floor(Math.random() * arr.length);
        [arr[n1], arr[n2]] = [arr[n2], arr[n1]];
    }
    return alterarLista(arr)
}



let bubble_sort = (arr) => {  //arr.sort((a,b) => a-b)  //poderia so fazer isso tbm
    const n = arr.length;
    for (let i = 0; i < n - 1; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
            }
        }
    }
    alterarLista(arr)
}


let selection_sort = (arr) => {
    const n = arr.length;
    for (let i = 0; i < n - 1; i++) {
        let min_idx = i;
        for (let j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        [arr[i], arr[min_idx]] = [arr[min_idx], arr[i]];
    }
    alterarLista(arr)
}




let quick_sort = (arr, inicio, fim) => {
    if (inicio < fim) {
        const pivo = particionar(arr, inicio, fim);
        quick_sort(arr, inicio, pivo - 1);
        quick_sort(arr, pivo + 1, fim);
    }
}

function particionar(arr, inicio, fim) {
    const pivo = arr[fim];
    let i = inicio - 1;

    for (let j = inicio; j < fim; j++) {
        if (arr[j] <= pivo) {
            i++;
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
    }

    [arr[i + 1], arr[fim]] = [arr[fim], arr[i + 1]];
    return i + 1;

}
// console.log(array,0, array.length -1 )



/////////////////////////////////////////

let swap = (x, y) => {
    [array[x], array[y]] = [array[y], array[x]]
    return array
}
// console.log(swap(0, 5, ...array))



