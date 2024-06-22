function twoSums(numbers, target){
   let result = []
   numbers.map((x, i) => {
    numbers.map((y, j) => {
        if(i != j && x + y == target){
            result = [i, j];
        }
    });
   });
   return result;
};