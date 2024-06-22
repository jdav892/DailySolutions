//function oddOrEven(array){
//    const initialVal = 0
//    if(array.reduce((a, b) => a + b, 0) % 2 === 0){
//        return "even"
//    }else{
//        return "odd"
//    }
//}
//Above was initial solution and below was refactor on submission
const oddOrEven = array => array.reduce((a,b) => a + b , 0) % 2 ? "even" : "odd"