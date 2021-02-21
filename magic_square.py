#magic square


m = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
col=[]
row=[]
digonal=[]
i=0
while i<len(m):
    j=0
    sum_row=0
    sum_col=0
    sum_digonal=0
    while j<len(m[i]):
        sum_row=sum_row+m[i][j]
        sum_col=sum_col+m[j][i]
        sum_digonal=sum_digonal+m[i][j]
        j=j+1
    col.append(sum_col)
    row.append(sum_row)
    digonal.append(sum_digonal)
    
    i+=1

print(sum_row)
print(sum_col)

if row==col:
    print("it is magic square")
else:
    ("it is not")
