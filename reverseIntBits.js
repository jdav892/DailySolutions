function reverseBits(n){
    let nToBin = (n).toString(2)
    let rev = nToBin.split("").reverse().join("")
    return parseInt(rev, 2)
}