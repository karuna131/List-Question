#negetive,positive,zero

li=[20,30,-40,0,22,-12,0,-45,56]
i=0
positive=0
negative=0
zero=0
length=len(li)
while i<length:
    if 0<li[i]:
        positive=positive+1
        #print("",li[i], " positivehe")
    elif 0>li[i]:
        negative=negative+1
        #print(li[i]," negative he")
    else:
        zero=zero+1
        #print("",li[i],"  zero he")
    i+=1
print(positive,"positive numbers")
print(negative,"negative numbers")
print(zero,"zero numbers")