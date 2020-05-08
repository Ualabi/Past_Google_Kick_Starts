#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
 
typedef long long ll;
 
const int MAXK = 1e5;
ll a[MAXK+1], b[MAXK+1];
 
int pow_mod(int x, int n, int K){
    if (K==1)
        return 0;
    
    int ans = 1;
    while (n) {
        if (n&1)
            ans = (ll)ans*x%K;
        x = (ll)x*x%K;
        n >>= 1;
    }
    return ans;
}
 
int main(){
    const ll l = 1e9 + 7;
    
    int x, y;
    int T;
    int A, B;
    ll N,K;
    ll ans;
    ll aux;
    cin >> T;
    for (int i = 1; i <= T; i++){
        memset(a, 0, sizeof(a));
        memset(b, 0, sizeof(b));
 
        cin >> A >> B >> N >> K;
        ans = 0;
        aux = 0;
        for (x = 1; x <= min(N, K); x++){
            ll cnt = ((N - x) / K + 1) % l;
            int i = pow_mod(x, A, K), j = pow_mod(x, B, K);
            a[i] += cnt;
            b[j] += cnt;
            if ((i+j) % K == 0)
                aux = (aux+cnt)%l;
        }

        for (x = 0; x < K; x++){
            y = (K-x) % K;
            ans += ((a[x] % l) * (b[y] % l)) % l;
            ans %= l;
        }
 
        ans -= aux;
        ans += l;
        ans %= l;
 
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}