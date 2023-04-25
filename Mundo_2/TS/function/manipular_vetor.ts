function somatorio(pvetor: number[]): number {
    let soma: number = 0 ;
    for (var i of pvetor){
        soma += i;
    }
    return soma;
}

let pvetor: number[] = [1,2,3,4,5];
let res_soma: number = somatorio(pvetor)
console.log(`O resultado do somatório dos elementos do vetor ${pvetor} é: ${res_soma}`);






