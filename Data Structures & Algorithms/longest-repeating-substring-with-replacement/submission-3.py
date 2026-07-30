class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = defaultdict(int) #Char -> num of occurances
        maxOcc = 0
        for n in s :
            hm[n] += 1
            maxOcc = max(maxOcc, hm[n])
        maxChar = None
        for n in s :
            if hm[n] == maxOcc :
                maxChar = n
                break
        print (maxChar)
        l=0
        r=0
        longest = 0
        queue = []
        while r < len(s) :
            if s[r] != maxChar:
                queue.append(r)
                if k > 0 :
                    k -= 1
                    r += 1
                    longest = max(longest, r-l)
                else: 
                    longest = max(longest, r-l)
                    l = queue.pop(0) + 1
                    r+=1
            else :
                r += 1
                longest = max(longest, r-l)


        return longest
        