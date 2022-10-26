def countIncreasing(arr, n) -> int:
    cnt = 0
    for i in range(0, n) :
        for j in range(i + 1, n) :
            if arr[j] > arr[j - 1] :
                cnt += 1
            else: 
                break
    return cnt
n,q = map(int, input().split())
a = list(map(int, input().split()))
for j in range(q):
    x,y,z = map(int, input().split())
    if x == 1:
        continue
    elif x == 2:
        b = a[y:z]
        print(countIncreasing(b,len(b)))