comp(array1, array2);{
if(!array1 || !array2 || array1.length !== array2.length){
    return false;
}
const squared = array2.map(element => Math.pow(element, 0.5));
array1.sort((x, y) => x - y)
squared.sort((x, y) => x - y)
return array1.every((value, index) => value === squared[index]);

}