X=int(input())
L=list(map(int,input().split()))
Y=max(L)
L.remove(Y)
Z=max(L)
print(Y+Z)
