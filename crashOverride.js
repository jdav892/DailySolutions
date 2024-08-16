const firstLetter = str => str[0].toUpperCase()
const isValid = name => /[a-z]/gi.test(name)
const aliasGen = (first, last) =>
    isValid(first[0]) && isValid(last[0])
? `${firstName[firstLetter(first)]} ${surname[firstLetter(last)]}`
: "Your name must start with a letter from A - Z."