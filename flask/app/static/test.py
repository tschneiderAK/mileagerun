
def fuckoff(arr, k, x):
    n = len(arr)
    def bsearch(arr, x):    
        l = 0
        r = len(arr)-1

        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == x:
                return mid
            if x < arr[mid]:
                r = mid -1
            else:
                l = mid +1
        if l > 0:
            l -= 1
        if r < n:
            r +=2
        close = [(i, arr[i]) for i in range(l,r)]
        close.sort(key= lambda y: abs(y[1]-x))
        return close[0][0]

    closest = bsearch(arr, x)
    ans = [arr[closest]]

    cl = closest -1
    cr = closest + 1
            
    while len(ans) < k:
        if cl < 0:
            ans.append(arr[cr])
            cr += 1
        elif cr >= n:
            ans.append(arr[cl])
            cl -= 1
        elif abs(arr[cl]-x) <= abs(arr[cr]-x):
            ans.append(arr[cl])
            cl -= 1
        else:
            ans.append(arr[cr])
            cr += 1

    ans.sort()
    return ans

fuckoff([1,2,3,4,5],4,6)