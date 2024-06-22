function squareDigits(num){

const sq = Array.from(String(num), Number);
const sqn = sq.map(num => num**2);
const result = sqn.join('')
const resultInt = parseInt(resultString, 10);
return resultInt;
}