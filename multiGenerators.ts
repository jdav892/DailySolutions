export function* generator(a: number): Generator<string> {
    let count: number = 0
    while(true){
        yield `${a} x ${++count} = ${a * count}`
    }
}