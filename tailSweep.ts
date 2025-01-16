export function tailSwap(arr: [string,string]): [string,string] {
    const [prefix1, suffix1] = arr[0].split(":")
    const [prefix2, suffix2] = arr[1].split(":")

    let result1 = `${prefix1}:${suffix2}`
    let result2 = `${prefix2}:${suffix1}`

    return [result1, result2]
}