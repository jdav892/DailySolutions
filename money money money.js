function calculateYears(principal, interest, tax, desired) {
    let P = principal
    let Y = 0;
    while (P < desired) {
    let earned = P * interest;
      let deduct = earned * tax;
      P += earned - deduct;
       Y++;
  }
  return Y;
}