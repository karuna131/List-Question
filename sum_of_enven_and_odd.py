#count and addition of even and odd numbers.

n=[6,5,2,3,8,9,5,3,3,17,2,15,3,4,5,6,7,23,7,8,20,9,9,]
i=0
sum=0
add=0
even=0
odd=0
while i<len(n):
    if n[i]%2==0:
        even+=1
        sum=sum+n[i]
        sum+=1

    else:
        odd+=1
        add=add+n[i]
        add+=1
    i+=1
print(even,"numbers are even and total number sum is",sum)
print(odd,"numbers are odd and that numbers sum is",add)
