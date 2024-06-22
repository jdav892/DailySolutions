function isIsogram(str){
    return !str.match(/([a-z]).*\1/i);
  }


// Probably a better solution
//function isIsogram(str){
//    return new Set(str.toUppercase()).size === str.length;
//}
//
//
//  