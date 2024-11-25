export function flyBy(lamps: string, drone: string): string {
    let result = ""
    for(let i = 0; i < lamps.length; i++){
        if(i < drone.length){
            result += "o"
        }else{
            result += "x"
        }
    }
    return result
}