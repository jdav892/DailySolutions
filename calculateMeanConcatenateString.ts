export function mean(lst: string[]): [number, string] {
    let count: number = 0;
    let store: string = "";

    for(let i = 0; i < lst.length; i++){
        const num = Number(lst[i])
        if(!isNaN(num)){
            count += num
        }
        if(isNaN(num)){
            store += lst[i]
        }
    }
    let mean: number = count/10
    return [mean, store]
}