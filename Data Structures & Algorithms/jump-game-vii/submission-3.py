class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp=[False for _ in range(len(s))]

        dp[0] = True
        #[T,F,F,F,T,F,F,T]
        #[0,0,1,1,0,0,1,0]
        #           ^   ^ 
        #count = 3
        window = maxJump - minJump
        i = minJump
        count = window+1
        while i<len(s):

            while i<len(s) and count:
                if s[i] == '0':
                    dp[i] = True
                if dp[i-window]:
                    count = window+1
                count -= 1
                i += 1

            if dp[i-minJump]:
                count = window+1
            else:
                i+=1
        
        
        
        return dp[-1]
        # [T,T,F,F,F]
        # [0,0,0,0,0]
        #    ^ ^
        # count = 0
        