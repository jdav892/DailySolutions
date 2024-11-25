export function rakeGarden(garden:string):string {
    let strArr: string[] = garden.split(" ");
    for(let i = 0; i < strArr.length; i++){
        if(strArr[i] !== "gravel" || strArr[i] !== "rock"){
            strArr[i] = "gravel"
        }
    }
    return strArr.join(" ")
}