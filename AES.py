import math
def stToLis(s):
    ls = []
    for i in range(len(s)):
        ls.append(s[i])
    return ls     
def zeroAdds(s):
    s1 = len(s)
    if(s1 != 32):
        for i in range((32-s1)):
            s.insert(0,"0")
    return s 
def lsTostr(s):
    res = ""
    for i in range(len(s)):
        res+=s[i]
    return res    
def stXor(s,s1):
    if( s == "1"):
        if(s1 == "0"):
            return "1"
        elif(s1=="1"):
            return "0"
    elif(s=="0"):
        if(s1 == "0"):
            return "0"
        elif(s1=="1"):
            return "1"
    
    return "-1"        
def fullStXor(s,s1):
    k = ""
    for i in range(len(s)):
        k += stXor(s[i],s1[i])
    return k 
def hexaToBin(s):
    n = int(s, 16) 
    bStr = ''
    while n > 0:
    	bStr = str(n % 2) + bStr
    	n = n >> 1	
    res = bStr
    return  str(res)


lshex = ["2475A2B3","34755688","31E21200","13AA5487"]
lsbin = [] 
for  i in range(len(lshex)):
    k = hexaToBin(lshex[i])
    k1 = stToLis(k)
    z = zeroAdds(k1)
    l = lsTostr(z)
    lsbin.append(l)


t1 = "ad20177d"
t1bin = hexaToBin(t1)
# round 1: 

final1 = []
k89 =0 
k98 = 1
final1.append(fullStXor(t1bin,lsbin[0]))
for i in range(1,len(lshex)):
    final1.append(fullStXor(final1[k89],lsbin[k98]))
    k89 +=1
    k98 +=1
print(final1)
