#include <vector>
#include <cmath>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

class Solution{
    public:
        long solve(long A, long B, long C);
};


vector<long> factmod(long A, long C, long r){
    vector<long> answer = {};

    if(A == 0 or A == 1){

        answer.push_back(1);
        answer.push_back(1);
        answer.push_back(1);

        return answer;
    }

    long ans = 1;
    long k = 1;
    long ans_2 = 1;
    long ans_3 = 1;

    while(k<=A){
        ans = (ans*k)%C;
        if(k == r){
            ans_2 = ans;
        }
        if(k == A-r){
            ans_3 = ans;
        }
        k += 1;
    }
    answer.push_back(ans);
    answer.push_back(ans_2);
    answer.push_back(ans_3);

    return answer;
};

long powmod(long A,long B,long C){

    if(A == 0){
        return 0;
    }
    
    if(B == 0 or A == 1){
        return 1;
    }
    
    long sa = powmod(A,long(B/2),C);
    
    if(B%2 == 0){
        return (sa*sa)%C;
    }
    
    else{
        return ((sa*sa)%C*(A%C))%C;
    }
    
};

int main(){

    Solution s;

    long A = 6;
    long B = 2;
    long C = 13;

    cout<<s.solve(A,B,C);
    return s.solve(A,B,C);
};

long Solution::solve(long A, long B, long C) {
        vector<long> ans;
        ans = factmod(A,C,B);

        long n = ans[0];
        long r = ans[1];
        long n_r = ans[2];

        long a = powmod(n_r,C-2,C);
        long b = powmod(r,C-2,C);
        return ((n*a)%C*b)%C;
};
