function findNeedle(haystack){
    let stack = [...haystack];
    return `found the needle at position ${haystack.findIndex(item => item === 'needle')}`
}