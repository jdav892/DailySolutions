class Solution 
{
    public:
        int smallestNumber(int n)
        {
            int i = 10;
            for(i = 10; i >= n; i--)
            {
                if(pow(2, i) <= n) break;
            }
            cout << 1;
            return pow(2, i + 1) - 1
        }
}