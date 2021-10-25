n=int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
if len(arr)<1:
    print(arr[0])
else:
    j=1
    for i in range(n-1):
        if arr[j]>0  and arr[i]<0:
            arr[j]=arr[j]-arr[i]
        elif arr[j]<0  and arr[i]>0:
            arr[j]=arr[i]-arr[j]
        else:
            arr[j]=arr[j]+arr[i]
        j+=1
print(arr[-1])