var isAnagram = function(test, original){
    let testCase = test.toLowerCase()
    let originalCase = original.toLowerCase()

    let sortedTest = testCase.split('').sort().join('')
    let sortedOrigin = originalCase.split('').sort().join('')

    return sortedTest === sortedOrigin

};