function validateHello(greetings){
    const greets = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]
    const lowerGreet = greetings.toLowerCase()
    return greets.some(greeting => lowerGreet.includes(greeting))
}