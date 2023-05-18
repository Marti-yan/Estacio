texto = "Podemos ir Andando e andando chegaremos mais longe"
result = texto.replace(/andando/gi,"correndo");
console.log(result); // Podemos ir correndo e correndo chegaremos mais longe

texto2 = "12:34"
result = texto2.replace(/(..):(..)/,'$1h $2min'); //Formatação de horário
console.log(result); // 12h 34min


function data_por_extenso(texto_casado, grupol, grupo2, grupo3) {

    var dia = grupol;
    var mes = grupo2;
    var ano = grupo3;
    var meses = {
       '01':'Janeiro', '02':'Feveveiro', '03':'Março',
       '04':'Abril', '05':'Maio', '06':'Junho',
       '07':'Julho', '08':'Agosto', '09':'Setembro',
       '10':'Outubro', '11':'Novembro', '12':'Dezembro'
    };
    return dia + " de " + meses[mes] + " de " + ano;
}

console.log()

texto= "Hoje é dia 02/05/2023.";
regex = /(\d\d)\/(\d\d)\/(\d\d\d\d)/;
result = texto.replace(regex, data_por_extenso);
console.log(result); // Hoje é dia 10 de Maio de 2022.

console.log()

texto= "Amanhã é dia alegria.";
regex = /\w/g  //Apenas o barra-letra não é suficiente para casa com letras acentuadas
result = texto.replace(regex, '-');
console.log(result);  // -----ã é --- -------.

regex = /[\wÁ-ü]/g //Dessa forma vai casar com os caracteres acentuados
result = texto.replace(regex, '-');
console.log(result); // ------ - --- -------.