#include<bits/stdc++.h>
#include<string.h>
#define ll long long int
#define pb push_back
#define pf push_front
#define vi vector 
#define ff first
#define ss second
#define MX 1000000007
#define _GLIBCXX_DEBUG 1
const int p = 1e6+5 ;
using namespace std ;


void solve() 
{    
     
   ll n , x ,y ;
   cin >> n >> x ;
   vi <pair<ll,ll>> v ;
   ll sum = 0 ;
   for( int i = 0 ; i < n ; i ++ ){ cin >> y ; v.pb({y,1}) ; }
   ll i = 0 , s = n-1 ; 
   while( i <= s )
   {
    if( v[i].ff % x != 0 ){ break ; }
    else{
        ll c =  ( v[i].ff/x ) ;
        v.pb({c,x*v[i].ss}) ;
        s ++ ;
    }
    i ++ ; 
   } 
   for( ll i = 0 ; i <= s ; i ++ )
   {
    sum += (v[i].ff * v[i].ss) ;
   }
   cout << sum ;
       
}   

 
int main()
{
    ios_base::sync_with_stdio(false) ;
    cin.tie(NULL); 
    cout.tie(NULL) ;
 
#ifndef ONLINE_JUDGE    
    //for getting input from input.txt
    freopen("inputA.txt","r",stdin);
    //for getting output from output.txt
    freopen("outputA.txt","w",stdout);
#endif
       int t ; cin >> t ;
       
       
             
       while( t-- )
        {
            
            solve() ;
            cout <<"\n" ;

           
            
        }
        
    
    return 0 ;
}