elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
count=0
sum=0
even=0
sum1=0
odd=0
sum2=0
while i<len(elements):
    count=count+1
    sum=sum+elements[i]
    if elements[i]%2==0:
        sum1=sum1+elements[i]
        even=even+1
        sum1+=1
    else:
        sum2=sum2+elements[i]
        odd=odd+1
        sum2+=1
    i+=1
average=sum/len(elements)
average1=sum1/even
average2=sum2/odd
print("Total numbers :",count )
print("Sum of total number :",sum)
print("Average of total numbers :",average)
print("Total even numbers :",even)
print("Total sum of even numbers :",sum1)
print("Average of even numbers :",average1)
print("Total odd numbers :",odd)
print("Total sum of odd numbers :",sum2)
print("Average of odd numbers :",average2)


