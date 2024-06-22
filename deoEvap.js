function evaporator(content, evap_per_day, threshold){ 
  let result = 0;
  let percent = 100;
  while(percent > threshold){
    percent = percent - percent * (evap_per_day/100) 
    result += 1;  
  }
  return result
}