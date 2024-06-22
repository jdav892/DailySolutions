// var humanYearsCatYearsDogYears = function(humanYears){
//     let catYears = 0;
//     let dogYears = 0;

//     if(humanYears >= 1)
//     catYears += 15;
//     dogYears += 15;

//     catYears += 9;
//     dogYears += 9;

//     catYears += 4 * (humanYears - 2);
//     dogYears += 5 * (humanYears - 2);

//     return [humanYears, dogYears, catYears]
// }

var humanYearsCatYearsDogYears = function(humanYears){
    let catYears = 0;
    let dogYears = 0;

    if(humanYears >= 1){
        catYears += (humanYears >= 2) ? 24 : 15;
        dogYears += (humanYears >= 2) ? 24 : 15;

        catYears += 4 * Math.max(humanYears - 2, 0);
        dogYears += 5 * Math.max(humanYears - 2, 0)
    }
    return [humanYuears, catYears, dogYears]
}
