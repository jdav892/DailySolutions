function boredom(staff){
    const boredom = {
        accounts: 1,
        finance: 2,
        canteen: 10,
        regulation: 3,
        trading: 6,
        change: 6,
        IS: 8,
        retail: 5,
        cleaning: 4,
        "pissing about": 25
      }
      let total = 0;
      for(let name  in staff){
        let department = staff[name];
        total += boredom[department] || 0;
      }
      if(total <= 80){
        return 'kill me now'
      }else if(total < 100 && total > 80){
        return 'i can handle this'
      }else{
        return 'party time!!'
      }
}