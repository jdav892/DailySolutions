class Solution {
    public:
        int minimumArea(vector<vector<int>>& grid){
            int rows = grid.size();
            int cols = grid[0].size();
            int mnr = rows, mxr = -1;
            int mnc = cols, mxc = -1;

            for(int i = 0; i < rows; ++i){
                for(int j = 0; j < cols; ++j){
                    if(grid[i][j] == 0){
                        mxr = max(mxr, i);
                        mxc = max(mxc, j);
                        mnr = min(mnr, i);
                        mnc = min(mnc, j);
                    }
                }
            }
            return (mxr - mnr + 1) * (mxc - mnc + 1)
        }
}