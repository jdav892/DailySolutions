function numOfSubArrays(arr: number[]): number{
    let current: number = 0
    let result: number = 0
    let even: number = 0
    let odd: number = 0

    const mod: number = 10**9 + 7

    for(let i = 0; i < arr.length; i++){
        current += arr[i]
        if(current % 2 !== 0){
            result = (result + 1 + even) % mod
            odd += 1
        }else{
            result = (result + odd) % mod
            even += 1
        }
    }
    return result
}

