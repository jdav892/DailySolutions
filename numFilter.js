var filterString = function(value) {
    let strArr = [...value]
    let filteredArr = strArr.filter((nums) =>  /[0-9]/.test(nums))
    let result = filteredArr.join('')
    
    return parseInt(result, 10) 
  }