function cubeChecker(volume, side){
  if(volume <= 0){
    return false
  }else if(volume === side ** 3){
    return true;
  }else{
    false;
  }
};