list1=[1,2,3,4,10,6]
list2=[3,2,1,6,7,8]
num=[]
i=0
while i<len(list1):
    if list1[i] in list2:
        pass
    else:
        num.append(list1[i])
        print(list1[i])
    i+=1