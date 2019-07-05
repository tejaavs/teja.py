men = int(input())
nis = list(map(int,input().split()))
nis.sort()
a = []
for i in range(len(nis)-1):
    if nis[i]==nis[i+1]:
        a.append(nis[i])
if a:
    for x in  set(a):
        print(x,end=" ")
else:
    print("unique")
