function multipleOfIndex(array){
    return array.filter((element, index) => element % index === 0 || element === 0);
}