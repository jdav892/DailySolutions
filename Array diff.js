function arrayDiff(a, b){
    const diff = a.filter((e) => !b.includes(e));
    return diff
}