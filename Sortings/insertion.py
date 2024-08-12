def insertion(arr):
    n=len(arr)
    for i in range(n):
        j=i
        while j >0 and arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j=j-1
    return arr
a=input()
arr=[int(x) for x in a.split()]
res=insertion(arr)
print(res)