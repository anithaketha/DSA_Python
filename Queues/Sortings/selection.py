def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr
a=input()
arr=[int(x) for x in a.split()]
res=selection_sort(arr)
print(res)