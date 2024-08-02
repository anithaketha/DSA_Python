def knows(mat,el1,el2):
    return mat[el1][el2]==1
def celebrity(mat,n):
    stack=[]
    for i in range(n):
        stack.append(i)
    while len(stack)!=1:
        el1=stack.pop()
        el2=stack.pop()
    if knows(mat,el1,el2):
        stack.append(el2)
    else:
        stack.append(el1)
    #verfication
    zero=0
    ones=0
    #for celebrity el na rows anni-> 0
    #cols na anni->1
    ans=stack[-1]
    for i in range(n):
        if mat[ans][i]==0:
            zero+=1
    if zero!=n:
        return -1
    for i in range(n):
        if mat[i][ans]==1:
            ones+=1
    if ones!=n-1:
        return -1
    return ans
n=int(input())
rows=int(input())
cols=int(input())
matrix=[]
for i in range(rows):
    row_input=input().strip()
    row=[int(i) for i in row_input.split()]
    matrix.append(row)
print(matrix)
res=celebrity(matrix,n)
print("The celebrity is",res)