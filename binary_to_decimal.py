a= [1, 0, 0, 1, 1, 0, 1, 1]
i=1
sum=0
k=0
while i<=len(a):
    b=(2**k)*a[-i]
    sum+=b
    i+=1
    k+=1
print(sum)