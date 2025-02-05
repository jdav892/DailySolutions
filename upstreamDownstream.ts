export function time(distance:number,boatSpeed:number,stream:String):number{
    let streamArr: string[] = stream.split(" ");
    let streamVal: number = Number(streamArr[1])
    if(streamArr[0] === "Downstream"){
        boatSpeed += streamVal
    }
    if(streamArr[0] === "Upstream"){
        boatSpeed -= streamVal
    }
    return parseFloat((distance/boatSpeed).toFixed(2))
}