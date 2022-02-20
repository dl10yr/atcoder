n=int(input())
a=list(map(int,input().split()))

q=[]
 
cnt=0
 
for i in range(n):
    cnt+=1
    if len(q)==0:
        q.append((a[i],1))
    else:
        pop=q.pop()
        if pop[0]==a[i]:
            if pop[1]+1==a[i]:
                cnt-=a[i]
            else:
                q.append((a[i],pop[1]+1))
        else:
            q.append(pop)
            q.append((a[i],1))
    print(cnt)