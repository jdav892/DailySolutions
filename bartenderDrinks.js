function getDrinkByProfession(param){
  let checker = param.toLowerCase()
  
  if(checker == "jabroni"){
    return "Patron Tequila"
  }else if(checker == "school counselor"){
    return "Anything with Alcohol"
  }else if(checker == "programmer"){
    return "Hipster Craft Beer"
  }else if(checker == "bike gang member"){
    return "Moonshine"
  }else if(checker == "politician"){
    return "Your tax dollars"
  }else if(checker == "rapper"){
    return "Cristal"
  }else{
    return "Beer"
  }
}