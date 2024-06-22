function feast(beast, dish){
    if(beast.substring(0, 1) === dish.substring(0, 1) && beast.substring(beast.length -1) === dish.substring(dish.length -1)){
        return true;
    }else{
        return false;
    }
}