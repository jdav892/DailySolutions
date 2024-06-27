function calculateTip(amount, rating) {
let rRating = rating.toLowerCase()
  if(rRating === "terrible"){
  return Math.ceil(amount*0)
  }else if(rRating === "poor"){
    return Math.ceil(amount*.05)
  }else if(rRating === "good"){
    return Math.ceil(amount*0.1)
  }else if(rRating === "great"){
    return Math.ceil(amount*0.15)
  }else if (rRating === "excellent"){
    return Math.ceil(amount*0.2)
  }else{
    return "Rating not recognised"
  }
}