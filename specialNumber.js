function specialNumber(n){
    return n.toString().split('').every(num => '012345'.includes(num))
        ? "Special!!"
        : "NOT!!";
}