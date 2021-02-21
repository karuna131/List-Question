#Kitne Crorepati, kitne Lakhpati, kitne Diwaliya.

kitne= [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100] 
i=0
cror=0
lakh=0
dilwale=0
while i<len(kitne):
    if kitne[i]>=10000000:
        cror=cror+1
    elif kitne[i]<10000000 and kitne[i]>=100000:
        lakh=lakh+1
    else:
        dilwale=dilwale+1
    i+=1
print(cror," people are Crorpati")
print(lakh," people are Lakhpati")
print(dilwale," people are Dilwale")