//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{

	public:
	int minCoins(int coins[], int M, int V) 
	{ 
	    // Your code goes here
	    int t[M+1][V+1];
	    for(int i=0;i<=M;i++){
	        for(int j=0;j<=V;j++){
	            if(j==0) t[i][j] = 0;
	            else if(i==0) t[i][j] = INT_MAX-1;
	            else if(coins[i-1] <= j){
	                t[i][j] = min(1+t[i][j-coins[i-1]],t[i-1][j]);
	            }
	            else t[i][j] = t[i-1][j];
	        }
	    }
	    if (t[M][V] == INT_MAX - 1)
        return -1;
	    
	    return t[M][V];
	}
	  
};

//{ Driver Code Starts.
int main() 
{
   
   
   	int t;
    cin >> t;
    while (t--)
    {
        int v, m;
        cin >> v >> m;

        int coins[m];
        for(int i = 0; i < m; i++)
        	cin >> coins[i];

      
	    Solution ob;
	    cout << ob.minCoins(coins, m, v) << "\n";
	     
    }
    return 0;
}

// } Driver Code Ends