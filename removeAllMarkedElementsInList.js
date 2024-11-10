Array.prototype.remove_ = function(integer_list, values_list){
    return integer_list.filter(element => !values_list.includes(element));
  }
  