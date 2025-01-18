export function compare(s1:string|null, s2:string|null):boolean {
    if(s1 === null || s2 === null){
        return s1 === s2
    }

    const getSum = (str: string) => {
        let sum: number = 0
        for(let i = 0; i < str.length; i++){
            const charCode = str.toUpperCase().charCodeAt(i)
            if(charCode >= 65 && charCode <= 90){
                sum += charCode
            }else{
                return 0 
            }
        }
        return sum
    }

    return getSum(s1) === getSum(s2)
}