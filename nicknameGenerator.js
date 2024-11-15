function nicknameGenerator(name){
    let vowels = /[aeiou]/gi
    if(name < 4){
        return `Error: Name too short`
    }
    if(name[2].match(vowels)){
        return name.slice(0, 2)
    }
    if(!name[2].match(vowels)){
        return name.slice(0, 3)
    }
}