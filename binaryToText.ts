export function binaryToString(binary: string) {
    if(!binary) return "";

    const segments = binary.match(/.{8}/g) || [];
    //use {1.8} to assure 8 bit chunks if given input isn't clean

    return segments
        .map((segment) => String.fromCharCode(parseInt(segment, 2)))
        .join("");
  }