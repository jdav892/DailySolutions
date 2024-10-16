function calculate(str){
str = str.replace(/plus/g, "+").replace(/minus/g, "-")
    return eval(str).toString()
}
