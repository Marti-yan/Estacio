er = new RegExp('[A-Z]');

const regex = RegExp('foo*', 'g');

const str = 'table football, foosball'

while ((array = regex.exec(str)) !== null) {
    console.log(`Encontrado ${array[0]} Na posição de index = ${regex.lastIndex}.`)
}

console.log(regex.test(str));
console.log(regex.lastIndex);