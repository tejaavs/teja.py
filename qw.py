n1,n2=map(str,input().split())
if(len(n1)!=len(n2)):
    print("no")
x=[n1.count(i) for i in n1]
y=[n2.count(i) for i in n2]

if(x==y):
    print("yes")
else:
    print("no")
