export function dashatize(num: number) : string {
    if(num === 0) return "0"

    let numStr: string[] = Math.abs(num).toString().split("")
    let newArr: string[] = []

    for(let i = 0; i < numStr.length; i++){
        let current = numStr[i]
        let isOdd = Number(current) % 2 !== 0

        if(isOdd){
            if(newArr[newArr.length - 1] !== "-"){
                newArr.push("-")
            }
            newArr.push(current)
            if(i < numStr.length - 1){
                newArr.push("-")
            }
        }else{
            newArr.push(current);
        }
    }
    if(newArr[newArr.length - 1] === "-"){
        newArr.pop()
    }
    if(newArr[0] === "-"){
        newArr.shift()
    }
    return newArr.join("")
}