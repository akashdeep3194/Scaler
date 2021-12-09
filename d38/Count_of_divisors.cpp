#include <vector>
#include <cmath>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

vector<int> solve(vector<int> &A) {

        int mx = *max_element(A.begin(), A.end());
        cout<<mx<<"\n";
        vector<int> spf(mx+1,2);
        vector<int> res = {};

        spf[1] = 1;
        int i = 2;
        int j = i*2;

        while(i<=mx){

            j = i*2;

            while(j<=mx){
                spf[j] += 1;
                j += i;
            }

            i += 1;

        }            

        for(int k = 0; k<A.size();k++){
            res.push_back(spf[A[k]]);
        }
        return res;
}

int main()
{
    vector<int> arr1 = {9,10,121,168,25};
    vector<int> ans = solve(arr1);
    for(int i = 0;i<ans.size();i++)
    {
        cout<<ans[i]<<" ";
    }
}
