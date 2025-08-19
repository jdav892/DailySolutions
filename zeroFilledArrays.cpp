class Solution{
    public:
        long long zeroFilledArrays(vector<int>& nums) {
            int streak = 0;
            long long total = 0;
            for(int i = 0; i < nums.size(); i++){
                if(nums[i] == 0){
                    streak++;
                    total += streak;
                }else{
                    streak = 0;
                }
            }
            return total;
        };
};