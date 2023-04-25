let mediaFinal: number = 8.5;
if(mediaFinal == 10){
    console.log("Não fez mais q sua obrigação")
} else if (mediaFinal > 8){
    console.log("Dá pra melhorar")
}else if (mediaFinal >= 7){
    console.log("se reprovasse ia tomar uma coça")
}else {
    console.log("Não serve pra na msm né!")
}

let podeVotar: string;
let idade: number = 17;
podeVotar = (idade >= 16)? "Já pode votar corno" : "Muito kid pra votar ainda!";
console.log(podeVotar)