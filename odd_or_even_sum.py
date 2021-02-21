elements=[23,14,56,12,19,9,15,25,31,42,43]
i=0
odd=0
even=0
while i<len(elements):
    if elements[i]%2==0:
        even=even+elements[i]
        even+=1
    else:
        odd=odd+elements[i]
        odd+=1
    i+=1
print(even,"even number sum")
print(odd,"odd number sum")