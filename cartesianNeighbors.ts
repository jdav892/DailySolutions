export function cartesianNeighbor(x: number, y: number): number[][] {
    let newVals: number[][] = [[x - 1, y - 1], [x - 1, y], [x - 1, y + 1], [x, y - 1], [x, y + 1], [x + 1, y - 1], [x + 1, y], [x + 1, y + 1]] 
      return newVals
    }