s1='abcedefs'
s2='cadfas'
x=len(s1) if len(s2)>=len(s1) else len(s2)
l1=[0]*len(s1)
l2=[0]*len(s2)
d1={}
d2={}
cnt=0
y=0
for i in s1:
    d1[i]=0
for j in s2:
    d2[j]=0
for j in d2:
    if j not in d1:
        cnt+=1
print(cnt)
for i in range(x):
    if s2[i] in s1:
        l2[i]=1
        y=s1.index(s2[i])
        l1[y]=1
        print(y,'...')
        break

for i in range(y+1,x):
    if s2[i] in s1[y+1:] and s1[y+1:].index(s2[i])>=y:
        l2[i]=1
        l1[s1[y+1:].index(s2[i])+len(s1[:y+1])]=1
        y=s1[y+1:].index(s2[i])
print(l1,l2)
print(l1.count(0)+cnt)        


    
    
    