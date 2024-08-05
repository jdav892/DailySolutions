function fuelPrice(litres, pricePerLitre){
    let discount = Math.min(0.25, Math.floor(litres/2) *.05);
    let total = litres * (pricePerLitre - discount);
    return parseFloat(total.toFixed(2));
}