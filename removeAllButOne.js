function remove (string) {
 let removed = string.replaceAll('!', '')
 return removed + '!'
}

// const remove = string => string.replace(/!/g, '') + '!'