class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l,r = 0, len(arr)-1
        
        while l<r:
            mid = (l+r)//2
            if arr[mid] < x:
                l = mid+1
            elif arr[mid]>=x:
                r = mid

        ret = deque([])
        l = r-1
        print(r,l)
        while len(ret) < k:
            if r(l>=0 and abs(arr[l]-x) <= abs(arr[r]-x)):
                ret.appendleft(arr[l])
                l-=1
        
            else:
                ret.append(arr[r])
                r += 1
        
        return list(ret)