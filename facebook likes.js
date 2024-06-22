function likes(names){
    const likeNum = names.length;
    if(likeNum === 0){
        return 'no one likes this'
    }else if(likeNum === 1){
        return `${names[0]} likes this`
    }else if(likeNum === 2){
        return `${names[0]} and ${names[1]} like this`
    }else if(likeNum  === 3){
        return `${names[0]}, ${names[1]} and ${names[2]} like this`
    }else {
        return `${names[0]}, ${names[1]} and ${liker - 2} others like this`
    }
}
    

    

        
    


