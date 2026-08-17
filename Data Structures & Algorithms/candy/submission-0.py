class Solution:
    def candy(self, ratings: List[int]) -> int:

        que = []
        for i,rating in enumerate(ratings):
            heapq.heappush(que,[rating,i])
        
        candy = [1 for _ in range(len(ratings))]
        while que:
            rating,i = heapq.heappop(que)
            if i-1 >=0 and ratings[i-1] < ratings[i]:
                candy[i] = max(candy[i], candy[i-1]+1)
            if i+1 < len(ratings) and ratings[i+1] < ratings[i]:
                candy[i] = max(candy[i], candy[i+1]+1)
        
        return sum(candy)