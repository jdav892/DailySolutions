export const removeFire = (str: string): string => {
    let newStr = str.replace(/Fire/g, "~~")
    return newStr
}