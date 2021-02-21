#asending order


li=[2,5,7,1,9,5,3,5,4,6,8]
i=0
while i<len(li):
    j=0
    while j<len(li):
        if li[i]<li[j]:
            c=li[i]
            li[i]=li[j]
            li[j]=c
        j+=1
    i+=1
print(li)


#disending order

li=[2,5,7,1,9,5,3,5,4,6,8]
i=0
while i<len(li):
    j=0
    while j<len(li):
        if li[i]>li[j]:
            c=li[i]
            li[i]=li[j]
            li[j]=c
        j+=1
    i+=1
print(li)