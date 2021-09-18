n=6
arr=[[0,1,1,0,1,0],[0,1,1,0,1,0],[0,1,1,0,1,0],[0,1,1,0,1,0],[0,1,1,0,1,0],[0,1,1,0,1,0]]
sum=[]
for i in range(n-2):
    for j in range(n-2):
        sum.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
print(max(sum))