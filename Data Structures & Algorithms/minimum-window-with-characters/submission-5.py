class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) : return ""
        hav = defaultdict(int)
        ne = defaultdict(int)

        for i in t:
            ne[i] += 1
        print(ne) 

        l,r = 0,0
        target = 0
        minSub = [-1,-1]

        while r < len(s) :
            char = s[r]
            if char in ne :
                hav[char] += 1
                if hav[char] == ne[char] :
                    target += 1
                    while target == len(ne) :
                        if l-r+1  <= minSub[1] - minSub[0] +1 :
                            minSub = [l,r]
                            print("smaller")
                        if s[l] in hav :
                            hav[s[l]] -= 1
                            if hav[s[l]] < ne[s[l]] :
                                target -= 1 
                        l += 1
            r += 1
                
        print(minSub)            
        return s[minSub[0] : minSub[1]+1]
        
    