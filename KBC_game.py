question= [
    "How many continents are there?",  #first           
    "What is the capital of India?",   #second   
    "NG mei kaun se course padhaya jaata hai?" #third   
]

options= [#for first question
    ["Four", "Nine", "Seven", "Eight"],
    #for second questoin
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    # for third question
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
i=0
c=0
c1=1
count=0
while i<len(question):
    print(question[i])
    j=0
    op=1
    while j<=len(options):
        print(op,"",options[i][j])
        op+=1
        j+=1
    solution = [3, 4, 1] 
    op2=["1.Four","3.Seven","3.Chennai","4.Delhi","1.Software Engineering","4.Agriculture"]
    lifeline=input("you want life line 'Yes' or 'No' :")
    if lifeline=="yes":
        print("50-50")
        if count==0:
            print(op2[i+c])
            print(op2[i+c1])
            ans=int(input("select one option  :"))
            if ans==solution[i]:
                print("right")
                print("🥳🥳")
                count+=1
            else:
                print("your answer is wrong")
                break
        else:
            print("you already used life line")
            ans=int(input("select a number  :"))
            if ans==solution[i]:
                print("🥳🥳")
            else:
                print("your answer is wrong")
    elif lifeline=="no":
        ans=int(input("select one option  :"))
        if ans==solution[i]:
            print("right")
            print("🥳🥳")
        else:
            print("your answer is wrong")
            break
    else:
        print("somthing is wrong")


    
    c+=1
    c1+=1
    i+=1

