#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

int main()
{
    
    vector<int> g1;
    int n,t,p,a1=0,a2=0;
    cin>>n;
    for (int i=0;i<n;i++)
    {
        cin>>t;
        g1.push_back(t);
    }
    for (int i=0;i<n;i++)
    {
        cout<<g1[i];
    }
    cout<<"Enter the position";
    cin>>p;
    for(int i=0;i<=p;i++)
    {
        a1+=(g1[i]*pow(10,(p-i)));
    }
    for(int i=p+1;i<n;i++)
    {
        a2+=(g1[i]*pow(10,(n-i-1)));
    }
    cout<<a1+a2;
    return 0;
}