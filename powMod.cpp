long long powMod(long long n,long long k,const long long p){
    long long res = 1;
    while(k > 0){
        if(k&1) res = res*n%p;
        k >>= 1;
        n = n*n%p;
    }
    return res;
}
