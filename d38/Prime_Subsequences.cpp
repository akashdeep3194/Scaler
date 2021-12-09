#include <vector>
#include <cmath>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

class Solution{
    public:
        int solve(vector<int> &A);
    };

int main()
{
    Solution s;
    vector<int> A = {100, 89};
    cout<<s.solve(A);
}

int Solution::solve(vector<int> &A) {

        int mx = *max_element(A.begin(),A.end());
        mx = mx + 1;

        vector<bool> prime(mx,true);

        prime[1] = false;
        prime[0] = false;

        int i = 2;
        int j = 1;

        while(i*i<=mx)
        {
            j = i*i;
            while(j<mx)
            {
                if(prime[j] == true)
                {
                    prime[j] = false;
                }
                j += i;
            }
            i += 1;
        }
        
        long ctr= 0;
        long ans = 1;
        long C = 1000000007;
        long ele = 1;

        for(int k = 0;k<A.size();k++)
        {   
            ele = A[k];
            if(prime[ele])
            {
                cout<<ele<<"\n";
                ctr += 1;
                ans = (ans*2)%C;
            }
        }
        cout<<ctr;
        return  ans - 1;
}
