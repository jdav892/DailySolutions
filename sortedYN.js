function isSortedAndHow(array) {
  let ascend = array.slice().sort((a, b) => a -b)
  let descend = array.slice().sort((a, b) => b - a)
    if(array.join() === ascend.join()){
      return 'yes, ascending'
  }else if(array.join() === descend.join()){
      return 'yes, descending'
  }else{
    return "no"
  }
}