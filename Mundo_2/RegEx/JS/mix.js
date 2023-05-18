// A cadeia de nomes contém vários espaços e guias,
// e pode ter vários espaços entre o nome e o sobrenome.
var names = "José Silva ; Heitor Vasconcelos; Cristina Magalhães ; Abel Belarmino ; João Pitágoras ";
var output = ["---------- String original\n", names + "\n"];

// pattern: possível espaço em branco, em seguida, ponto e vírgula, em seguida, possível espaço em branco
var pattern = /\s*;\s*/;

// Quebra string em pedaços separados pelo padrão acima e
// armazena as partes em uma matriz chamada nameList
var nameList = names.split(pattern);

// novo pattern: um ou mais caracteres, espaços, caracteres acentuados ou não.
// Use parênteses para "memorizar" partes do padrão.
// As partes memorizadas são referenciadas mais tarde.
pattern = /([\wÁ-ü]+)\s+([\wÁ-ü]+)/;

// Nova matriz para armazenar nomes sendo processados.
var bySurnameList = [];
output.push("---------- Após Separar pela Expressão Regular");

for (let i = 0, len = nameList.length; i < len; i++){
  output.push(nameList[i]);
  bySurnameList[i] = nameList[i].replace(pattern, "$2, $1");
}

// Exibe a nova matriz.
output.push("---------- Nomes Invertidos");
for (i = 0, len = bySurnameList.length; i < len; i++){
  output.push(bySurnameList[i]);
}

// Classifica pelo sobrenome e exibe a matriz classificada.
bySurnameList.sort();
output.push("---------- Ordenado");
for (i = 0, len = bySurnameList.length; i < len; i++){
  output.push(bySurnameList[i]);
}

output.push("---------- Fim");

console.log(output.join("\n"))


//A expressão regular procura por zero ou uma ocorrência de parênteses de abertura \(?, 
//seguido de três dígitos \d{2}, seguido de zero ou uma ocorrência de parênteses de 
//fechamento \)?, seguido de um hífen, barra ou ponto decimal e, quando encontrado,  
//guarda o caractere ([-\/\.]), seguido de três dígitos \d{4,5}, seguido por um caractere  
//de hífen, barra ou ponto decimal que fora guardado \1, seguido por quatro dígitos \d{4}.
var re = /\(?\d{2}\)?([-\/\.])\d{4,5}\1\d{4}/;
function formataTelefone(phoneInput){
  console.log(phoneInput);
  var OK = re.exec(phoneInput);
  console.log(OK[0])
  if (!OK)
    //phoneInput.match(re);
    console.log(re + " Não é um número de telefone com código de área!");
  else
    console.log("Obrigado, o seu número de telefone é " + OK[0]);
}

//Os formatos esperados são ##-#####-#### ou ##-#####-####
formataTelefone("82-3333-5454");
formataTelefone("82-99833-5454");



function is_url(str)
{
  regexp =  /^(?:(?:https?|ftp):\/\/)?(?:(?!(?:10|127)(?:\.\d{1,3}){3})(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,})))(?::\d{2,5})?(?:\/\S*)?$/;
        if (regexp.test(str))
        {
          return true;
        }
        else
        {
          return false;
        }
}

console.log(is_url("http://www.google.com"));                 // true
console.log(is_url("https://aurelio.net/regex/javascript/")); // true
console.log(is_url("ftp://developer.mozilla.org"));         // true
console.log(is_url("168.1.1.200/aula"));                         // true