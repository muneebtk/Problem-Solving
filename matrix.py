rows=int(input('Enter rows : '))
cols=int(input('Enter column : '))

# main is the outer list
main=[]
# first create a matrix by rows X cols all the position have 0
for i in range(rows):
    lst=[]
    for j in range(cols):
        lst.append(0)
    main.append(lst)
# i represent the row index
i=0
# j represent the column index
j=0
# y is used to add the value in the matrix (increment by one)
y=1
# k is used to add  the index of column when the rows index is maximum
k=0

for h in range(cols+rows-1):
    if h<rows:
        i=h
    else:
        i=rows-1
    if i<rows:
        j=0
    else:
        j+=1
    if h>=rows:
        k+=1
        j+=k
    while i>=0 and j<cols:
        main[i][j]=y
        y+=1
        i-=1
        j+=1
for i in main:
    print(i)
