//function getMiddle(s)
//{
//  return s.slice((s.length-1)/2, s.length/2+1);
//}

function getMiddle(s){
    let midIndex = Math.floor(s.length/2);
    if(s.length % 2 === 1){
        return s.charAt(midIndex);
    }else{
    } return s.slice(midIndex - 1, midIndex + 1);
}