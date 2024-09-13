function kebabize(str){
    let replaced = str.replace(/\d+/g, '');
    let kebab = replaced
        .replace(/([A-Z])/g, '-$1')
        .toLowerCase();
    return kebab.startsWith('-') ? kebab.slice(1) : kebab
}