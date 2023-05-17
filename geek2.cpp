#include <iostream>
#include <vector>
#include <math.h>
using namespace std;
int main()
{
    
    string s;
    int ans[5],i=0;
    cout<<"Enter the string";
    cin>>s;
     for (auto& x : s) 
     {
        if(x==' ')
        {
            x='t';
        }
        x = tolower(x);
     }
    char vowel[5]={'a','e','i','o','u'};
    while(i<5)
    {
        int count=0;
        for(int x=0;s[x]!='\0';x++)
        {
            if(s[x]==vowel[i])
            {
                count++;
            }

        }
        ans[i]=count;
        i++;
    }
    int index;
    for(int i=0;i<5;i++)
    {
        index=i;
        for(int j=0;j<5;j++)
        {
            if(ans[index]<ans[j])
            {
                index=j;
            }
        }
        cout<<vowel[index]<<" "<<ans[index]<<"\n";
        ans[index]=-1;
    }

}