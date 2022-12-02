class Solution {
public:
    int maxSumAfterPartitioning(vector<int>& arr, int k) {
        int n = arr.size();
        vector<int> dp(k);
        
        for(int i=1;i<=n;++i){
            int highest = 0;
            int currMax = 0;
            for(int j=1;j<=k && i-j>=0;++j){
                currMax = max(currMax, arr[i-j]);
                highest = max(highest,dp[(i-j)%k]+currMax*j);
            }
            dp[i%k] = highest;
        }
        return dp[n%k];
    }
};