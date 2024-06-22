function vertMirror(strng){
    return strng.split("\n")
                .map(part => part.split("").reverse().join(""))
                .join("\n");
}

function horiMirror(strng){
    return strng.split("\n")
                .reverse()
                .join("\n");
}

function oper(fct, s){
    return fct(s);
}