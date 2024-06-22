 function descendingOrder(n){
return Number(n.toString().split('').sort((a, b) => b - a).join())
}

// const descendingOrder = (n) => Number([...("" + n)].sort().reverse().join(""))

