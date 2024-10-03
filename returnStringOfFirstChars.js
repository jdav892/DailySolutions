function makeString(s){
    let stringOfFirsts = s.split(" ");
    let firsts = stringOfFirsts.map(str => str.charAt(0));
    return firsts.join("");

}