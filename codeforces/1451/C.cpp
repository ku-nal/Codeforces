#include<bits/stdc++.h>
using namespace std;

int main(){
	#ifndef ONLINE_JUDGE
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
	#endif
	int t; cin>>t;
	while(t--){
		int n;cin>>n;
		int k;cin>>k;
		string fi; cin>>fi;
		string sec;cin>>sec;
		int a[26]={0};
		int b[26]={0};

		for(int i=0;i<n;i++){
			a[fi[i]-'a']+=1;
			b[sec[i]-'a']+=1;
		}

		for(int i=0;i<26;i++){
			if (i==25){
				if (a[i]==b[i]) cout<<"YES"<<endl;
				else cout<<"NO"<<endl;
			}
			if (a[i]<b[i]) {
				cout<<"NO"<<endl;
				break;
			}
			else if(a[i]>b[i]){
				int rem=a[i]-b[i];
				if((rem%k)==0){
					a[i+1]+=rem;
				}
				else{
					cout<<"NO"<<endl;
					break;
				}
			}
		}


	}
}

