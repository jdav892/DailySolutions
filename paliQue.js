function isPalindrome(x) {
let xu = x.toLowerCase();
  let reverse = xu.split('').reverse().join('');
  
  return xu === reverse
}