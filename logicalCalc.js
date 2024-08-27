function logicalCalc(array, op){
    if(op === "AND"){
        return array.reduce((acc, c) => acc && c);
    }else if(op === "OR"){
        return array.reduce((acc, c) => acc || c);
    }else if(op === "XOR"){
        return array.reduce((acc, c) => acc !== c);
    }
}