export function convert(n: string): string {
    let result: string = "";
    let i: number = 0;

    while(i < n.length){
        let asciiCode = parseInt(n.slice(i, i + 2), 10);
        
        if(asciiCode < 32 || asciiCode > 126){
            asciiCode = parseInt(n.slice(i, i + 3), 10);

            i += 3;
        }else {
            i += 2;
        }
        result += String.fromCharCode(asciiCode);
    }
    return result;
}