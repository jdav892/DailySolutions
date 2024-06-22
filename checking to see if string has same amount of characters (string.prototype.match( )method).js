function XO(str) {
  //replaced a line that converts to lowercase in favor of case insensitivity flag /i
    const countX = (str.match(/x/gi) || []).length;
    const countO = (str.match(/o/gi) || []).length;
      return countX === countO
    }

   // const XO = str = (str.match(/x/gi) || []).length === (str.match(/o/gi) || []).length