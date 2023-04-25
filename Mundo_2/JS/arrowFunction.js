let a = 5
let b = 8

function somar(a,b){
    return a + b;
}

let somar2 = (a,b) => {
    return a + b;
}

let somar3 = (a,b) => a + b;

console.log(somar(a,b))
console.log(somar2(a,b))
console.log(somar3(a,b))
