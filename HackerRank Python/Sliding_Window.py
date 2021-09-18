arr = list(map(int, input().rstrip().split()))
k=int(input())

#Normal method with Time complixity O(n^2)

# sum=0
# lsum=[]
# print(arr[:k])
# for i in range(len(arr)-k+1):
#     sum=0
#     for j in range(k):
#         sum+=arr[i+j]
#         lsum.append(sum) 
# print(max(lsum))



#Slicing Window method with Time complixity O(n)
window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(len(arr) - k):
    window_sum = window_sum - arr[i] + arr[i + k]
    max_sum = max(window_sum, max_sum)
 
print( max_sum)