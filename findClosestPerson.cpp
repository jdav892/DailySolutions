class Solution {
public:
    int findClosest(int x, int y, int z) {
        int xDiff = std::abs(z - x);
        int yDiff = std::abs(z - y);
        if (xDiff < yDiff){
            return 1;
        }else if (yDiff < xDiff) {
            return 2;
        }else {
            return 0;
        }
    }
};