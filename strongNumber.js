function strong(n) {

    function facto(num){
        if(num === 0 || num === 1) return 1;
        let result = 1;
        for(let i = 2; i <= num; i++){
            result *= i;
        }
        return result;
    }

    let digits = n.toString().split('');
    let sumOfFactorials = 0;

    for(let digit of digits){
        sumOfFactorials += facto(parseInt(digit));
    }

    if(sumOfFactorials === n){
        return "STRONG!!!!"
    }else{
        return "Not Strong !!";
    }


  }