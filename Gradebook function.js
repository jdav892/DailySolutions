
function getGrade (s1, s2, s3) {
    const all = (s1 + s2 + s3)/3;
      if(all >= 90 && all <= 100){
        return 'A'
      }else if(all >= 80 && all < 90){
        return 'B'
      }else if(all >= 70 && all < 80){
        return 'C'
      }else if(all >= 60 && all < 70){
        return 'D'
      }else{
        return 'F'
      }
      }


     // function getGrade (s1, s2, s3) {
     //   avg = (s1+s2+s3)/3;
     //   if (avg < 60)  return "F";
     //     else if (avg < 70) return "D";
     //     else if (avg < 80) return "C";
     //     else if (avg < 90) return "B";
     //     else return "A";
     // }


    // function getGrade (s1, s2, s3) {
    //    var s = (s1 + s2 + s3) / 3
    //    return s >= 90 ? "A" : s >= 80 ? "B" : s >= 70 ? "C" : s >= 60 ? "D" : "F"
    //  }