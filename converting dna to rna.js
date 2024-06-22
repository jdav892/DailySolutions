function DNAtoRNA(dna){
return dna.replace(/t/gi, "U")
}
//can also use replaceAll() however replace with global flag is faster in this instance 


const DNAtoRNA = dna => dna.replaceAll(/t/gi, 'U')