# https://www.hackerrank.com/challenges/fair-cut/problem?isFullScreen=true



 long long int min(long long int i, long long int k){
     long long int result = (i > k) ? k : i;
     return result;
 }

long long int fairCut(long long int k, vector<long long int> arr) {
   long long int n=arr.size();
   sort(arr.begin(),arr.end());
   vector<vector<long long int>> dp(n+1,vector<long long int>(k+1,1e18));
   dp[0][0]=0;

   for(long long int i=1;i<=n;i++)
   {
       for(long long int j=0;j<=min(i,k);j++)
       {
           
           dp[i%2][j]=min(dp[(i+1)%2][j]+j*arr[i-1]-(k-j)*arr[i-1],(j>0?dp[(i+1)%2][j-1]+(i-j)*arr[i-1]-(n-k-i+j)*arr[i-1]:(long long)1e18));
       }
   }
 return dp[n%2][k];
}
