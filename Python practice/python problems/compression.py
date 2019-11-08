

from collections import  Counter


def compression(string):
    ans = ''
    count=1
    for i in range(1,len(string)):
        if(string[i]==string[i-1]):
            count+=1
        else:
            ans=ans+string[i-1]+str(count)
            count=1
    ans = ans + string[i] + str(count)
    if(len(ans)<len(string)):
        return ans
    else:
        return  string


print(compression('aaabbbccaa'))


