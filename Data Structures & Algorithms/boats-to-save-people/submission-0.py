class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r = 0,len(people)-1
		
        ret =0
        while l<r:
            if people[l]+ people[r] <= limit:
                l+=1
                r-=1
            else:
                r-=1
            
            ret += 1

        if l == r: ret +=1
        return ret
