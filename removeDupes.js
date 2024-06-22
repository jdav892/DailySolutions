function distinct(a) {
 let noDubs = new Set ([...a])
 return [...noDubs];
}