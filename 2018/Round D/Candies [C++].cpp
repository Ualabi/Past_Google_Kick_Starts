// Link: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ee1/00000000000510ef

#include <iostream>
#include <algorithm>
#include <cassert>
#include <cstdio>
#include <vector>
#include <climits>
#include <numeric>
#include <set>
using namespace std;
using LL = long long;

LL solve(LL N, LL O, LL D, LL X1, LL X2, LL A, LL B, LL C, LL M, LL L){
    vector<LL> V(N);
    V[0] = X1; V[1] = X2;
    for (int i=2; i<N; ++i){
        V[i] = (A * V[i-1] + B * V[i-2] + C) % M;
    }
    for (auto &num: V)
        num += L;
    
    vector<int> ODD;
    ODD.push_back((V[0] + (1LL << 32)) % 2 == 1);
    for (int i=1; i<N; ++i)
        ODD.push_back(ODD.back() + (V[i] + (1LL << 32)) % 2);
    
    vector<LL> S;
    LL ans = LONG_LONG_MIN;
    partial_sum(V.begin(), V.end(), back_inserter(S));
    int cur = 0, nxt;
    multiset<LL> PS;
    for (int i=0; i<N; ++i){
        nxt = upper_bound(ODD.begin() + i, ODD.end(), (i ? ODD[i-1] : 0) + O) - ODD.begin();
        cur = max(cur, i);
        for (int j=cur; j<nxt; ++j){
            PS.insert(S[j]);
        }
        cur = nxt;
        LL max_val = (i ? S[i-1] : 0) + D;
        auto aux = PS.upper_bound(max_val);
        if (aux != PS.begin()) {
            ans = max(ans, *prev(aux) - (i ? S[i-1] : 0LL));
            assert(*prev(aux) - (i ? S[i-1] : 0LL) <= D);
        }
        if (PS.find(S[i]) != PS.end()) PS.erase(PS.find(S[i]));
    }
    return ans;
}

int main(){
    int T, t;
    LL ANS, N, O, D;
    LL X1, X2, A, B, C, M, L;
    
    cin >> T;
    for(t=0; t<T; t++){
        cin >> N >> O >> D;
        cin >> X1 >> X2 >> A >> B >> C >> M >> L;
        ANS = solve(N, O, D, X1, X2, A, B, C, M, L);
        cout << "Case #" << t+1 << ": ";
        if (ANS > LONG_LONG_MIN)
            cout << ANS << endl;
        else
            cout << "IMPOSSIBLE" << endl;
    }
}