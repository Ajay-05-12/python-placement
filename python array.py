n=int(input())
arr=list(map(int,input().split()))
s=0
for x in arr:
    print(s,end=" ")
    s=s+x
