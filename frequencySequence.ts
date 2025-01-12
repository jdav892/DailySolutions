export function freqSeq(str: string, sep: string): string {
    let newArr: string[] = []
    let strArr: string[] = str.split("")

    for(let i = 0; i < strArr.length; i++){
        const char = strArr[i]
        const count = (str.match(new RegExp(char.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "g")) || []).length;
        newArr.push(count.toString())
    }
    return newArr.join(`${sep}`)
}