function areAlmostEqual(s1: string, s2: string): boolean {
    let vals: number[] = []

    for(let i = 0; i < s1.length; i++){
        if(s1[i] !== s2[i]){
            vals.push(i)
        }

        if(vals.length > 2){
            return false
        }
    }
    return vals.length === 0 || (vals.length === 2 && s1[vals[0]] === s2[vals[1]] && s1[vals[1]] === s2[vals[0]])
}