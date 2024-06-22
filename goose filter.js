function gooseFilter(birds){
    var geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"];
    return birds.filter(birds => !geese.includes(birds));
}