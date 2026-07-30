
# n = 2
#    |   |   |

#    [1,2]
#          
#    [,3,2,1,0]
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        distWays = [0] * (n)
        distWays[0] = 1
        distWays[1] = 2
        for i in range(2,n):
            distWays[i] += distWays[i-1]
            if i-2 >= 0:
                distWays[i] += distWays[i-2]
        print(distWays)
        return distWays[-1]
        