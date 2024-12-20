export function dropCap(s: string): string {
    if(s === ""){
        return ""
    }

    const words = s.split(" ")

    return words.map((word) => {
        if(word.length > 2){
            word[0].toUpperCase() + word.slice(1).toLowerCase()
        }
        return word
    }).join(" ")
}