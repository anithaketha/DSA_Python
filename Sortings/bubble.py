def bubble(arr):
    n=len(arr)
    for i in range(n):
        swap=0
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
            swap=1
        if swap==0:
            break
    return arr
a=input()
arr=[int(x) for x in a.split()]
res=bubble(arr)
print(res)