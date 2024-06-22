function diamond(n){
    if(n % 2 === 0 && n < 0){
        return null
    }
    const line = lw =>
    ' '.repeat((n - lw) / 2) + '*'.repeat(lw) + "\n"
    let width = n - 2;
    let total = '*'.repeat(n) + "\n"

    while(width > 0){
        const newLine = line(width);
        total = newLine + total + newLine;
        width = width - 2;
    }
    return total;

}