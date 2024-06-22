var greet = function(name) {
  let nName = name.toLowerCase()
  return `Hello ${nName.charAt(0).toUpperCase()}${nName.slice(1)}!`
};
