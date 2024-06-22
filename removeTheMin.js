function removeSmallest(numbers) {
  if(numbers === 0){
    return [];
  }
let min = Math.min(...numbers);
let index = numbers.indexOf(min);

  if(index !== -1){
    numbers = numbers.filter((_, i) => i !== index);
  }
  return numbers
}