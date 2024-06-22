function animal(obj){
    let animal = {
        name: obj.name,
        legs: obj.legs,
        color: obj.color
    }
    return `This ${animal.color} ${animal.name} has ${animal.legs} legs.`
}

// Can use destructuring and do something along the lines of
//function animal(obj){
//const {name, color, legs } = obj
//return `This ${animal.color} ${animal.name} has ${animal.legs} legs.`
//}
//can also use let but const >>