export function calcType(a: number, b: number, res: number): string {
    if(a + b === res){
        return "addition"
    }else if(a - b === res){
        return "subtraction"
    }else if(a / b === res){
        return "division"
    }else if(a * b === res){
        return "multiplication"
    }else{
        throw new Error("Invalid")
    }
}