function abbrevName(name){
let words = name.split(' ')

let initials = words.map(word => word.charAt(0).toUpperCase());
 
  return initials.join('.')
}