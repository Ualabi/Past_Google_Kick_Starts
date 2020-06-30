// Link: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201ca2/0000000000201ca3
// Solution from: https://tinyurl.com/yd9gx4uo

#include <cstring>
#include <cstdio>
#include <queue>
#include <cmath>
using namespace std;
#define N 15

int id[N];
int T,n,m;
int k[N],level[N],a[N][N];
long long c[N][N];
long long p[N];
long long res = 0;

int onenum(int x){
    int res = 0;
    while (x) {
        res ++;
        x &= (x-1);
    }
    return res;
}

void dfs(int x,long long sum,int left){
    res = max(res,sum);
    if(x == 8)
        return;
    if(x && sum + p[7]-p[x-1] <= res)
        return;
    dfs(x+1,sum,left);
    for(int i = level[id[x]]+1;i<=k[id[x]];i++){
        if(left < c[id[x]][i])
            break;
        dfs(x+1, sum+a[id[x]][i]-a[id[x]][level[id[x]]], left-c[id[x]][i]);
    }
}

int main(){
    scanf("%d",&T);
    for(int z = 1;z<=T;z++){
        scanf("%d %d",&m,&n);           //Inputs
        for(int i = 0;i<n;i++){
            scanf("%d %d",&k[i],&level[i]);
            for(int j = 1;j<=k[i];j++)
                scanf("%d",&a[i][j]);
            for(int j = 2;j<=k[i];j++)
                scanf("%lld",&c[i][j]);
            for(int j = level[i]+2;j<=k[i];j++)
                c[i][j] += c[i][j-1];
        }
        
        res = 0;
        for(int i = (1<<8)-1;i<(1<<n);i++){// C(8,n)
            if(onenum(i) == 8){
                int tmp = 0;
                long long sum = 0;
                for(int j = 0;j<n;j++)
                    if((1<<j) & i)
                        id[tmp++] = j;
                for(int j = 0;j<8;j++)
                    sum += a[id[j]][level[id[j]]];
                
                p[0] = a[id[0]][k[id[0]]]-a[id[0]][level[id[0]]];
                for(int i = 1;i<8;i++)
                    p[i] = p[i-1] + a[id[i]][k[id[i]]]-a[id[i]][level[id[i]]];       
                dfs(0,sum,m);
            }
        }
        printf("Case #%d: %lld\n",z,res);
    }
    return 0;
}