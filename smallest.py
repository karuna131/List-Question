a=[2,3,4,5,5,6,7,7,1,8,8,98]
smallest=a[0]
i=0
while i<len(a):
    if a[i]<smallest:
        smallest=a[i]
    i+=1
print(smallest)