/**
 * @param {string} address
 * @return {string}
 */
var defangIPaddr = function(address) {
    let strArr = [];
    for(let i = 0; i < address.length; i++){
        if(address[i] === "."){
            strArr.push('[.]')
        }else{
            strArr.push(address[i])
        }
    }
    return strArr.join("")
}