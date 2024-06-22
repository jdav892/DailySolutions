function isValidWalk(walk){
    let nr = 0;
    let st = 0;
    let ws = 0;
    let es = 0;
        for(let dir of walk ){
            switch(dir){
                case 'n':
                    nr++;
                    break;
                case 's':
                    st++;
                    break;
                case 'w':
                    ws++;
                    break;
                case 'e':
                    es++;
                    break;
                    

            }
        }
        return(nr === st && es === ws && walk.length === 10);
}

//  function isValidWalk(walk){
//     let dx = 0
//     let dy = 0
//     let dt = walk.length
//      for(let i = 0; i < walk.length; i++){
//          switch(walk[i]){
//          case 'n': dy--; break
//          case 's': dy++; break
//          case 'e': dx--; break
//          case 'w': dx++; break
//         }
//     }
//  return dt === 10 && dx === 0 && dy  === 0
// }