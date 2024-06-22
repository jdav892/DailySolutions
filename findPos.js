function position(letter){
    const pos = 'abcdefghijklmnopqrstuvwxyz';
      for(let i = 0; i < pos.length; i++){
        if(letter === pos[i]){
         return `Position of alphabet: ${i + 1}` 
        }    
      }
    }