number=30
n=[10,11,12,13,14,17,18,19,20]
z=[]
i=0
while i<len(n):
    j=0
    while n[i]>n[j]:
        if number==n[i]+n[j]:
            z.append([n[j],n[i]])
        j+=1
    i+=1
print(z)
