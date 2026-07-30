class TimeMap:

    def __init__(self):
        self.tm = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tm[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        l1 = self.tm[key]
        l,r = 0, len(l1)-1


        while l < r:
            mid = (l+r)//2
            if timestamp == l1[mid][0] : return l1[r][1]
            if  timestamp < l1[mid][0]:
                r = mid-1
            elif timestamp > l1[mid][0] :
                l = mid+1
        
        return l1[r][1]
