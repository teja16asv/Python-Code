a = list(map(int,input().split()))
key = int(input())
l = []
for i in a:
    for j in a:
        if i+j == key and i != j:
            c = a.index(i)
            d = a.index(j)
l.append(c)
l.append(d)
l.sort()
for i in l:
    print(i,end=" ")