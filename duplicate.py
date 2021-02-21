#char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"] 
#output = [["a", 6], ["n", 3], ["t", 2], ["x", 2], ["u", 1], ["g", 1]]



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
    duple.append(count)
print([duple])
