#duplicate


char = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "t","w"]
i=0 
duple=[]
while i<len(char):
    j=0
    count=0
    while j<len(char):
        if char[i]==char[j]:
            count+=1
        j+=1
    if char[i] in duple:
        i+=1
        continue
    duple.append(char[i])
    print(char[i],"=",count)
print(duple)



# char = ["pooja","karuna","chhaya","pooja","saloni","karuna","pooja"]
# i=0 
# duple=[]
# while i<len(char):
#     j=0
#     count=0
#     while j<len(char):
#         if char[i]==char[j]:
#             count+=1
#         j+=1
#     if char[i] in duple:
#         i+=1
#         continue
#     duple.append(count)
#     #print(char[i],"=",count)
#     print(count,"",end="")
    


