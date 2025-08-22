function minimumArea(grid: number[][]): number {
    let rows = grid.length
    let cols = grid[0].length
    let mnx = rows, mxx = -1
    let mny = cols, mxy = -1

    for(let i = 0; i < rows; i++){
        for(let j = 0; j < cols; j++){
        if(grid[i][j] === 1){    
            mxx = Math.max(mxx, i)
            mxy = Math.max(mxy, j)
            mnx = Math.max(mnx, i)
            mny = Math.max(mny, j)
            }
        }
    }
    return (mxx - mnx + 1) * (mxy - mny + 1)
}