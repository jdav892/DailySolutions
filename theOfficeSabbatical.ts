export function sabb(s: string, val: number , happiness: number ): string{  
    let alphaArr: string[] = ["s", "a", "b", "t", "i", "c", "l"]
    let count: number = 0;
    let strArr: string[] = s.split("")
    for(let i = 0; i < strArr.length; i++){
      if(alphaArr.includes(strArr[i])){
        count += 1
      }
    }
    let total: number = val + count + happiness
    if(total > 22) return 'Sabbatical! Boom!'
    
    return 'Back to your desk, boy.'
    
  }