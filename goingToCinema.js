function movie(card, ticket, perc){
    let visits = 0
    let systemA = 0
    let systemB = card
    while(Math.ceil(systemA) <= Math.ceil(systemB)){
        visits += 1
        systemA = ticket * visits
        systemB += ticket * Math.pow(perc, visits)
    }
    return visits
}