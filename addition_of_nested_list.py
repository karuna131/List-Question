#addition of nested list


t=[[3,4,5,6,7],[7,5,3,4,9,],[5,8,3,2]]
i=0
sum=0
while i<len(t):
    j=0
    while j<len(t[i]):
        sum=sum+t[i][j]
        j+=1
    i+=1
print(sum)







     