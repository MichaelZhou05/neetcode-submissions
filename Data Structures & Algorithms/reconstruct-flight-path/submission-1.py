class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #build adj list

        tickets.sort()

        adjList = defaultdict(list)

        for from_i, to_i in tickets:
            adjList[from_i].append(to_i)

        
        res = ["JFK"]
        def dfs(node) -> bool:
            if len(res) == len(tickets) + 1:
                return True
            if len(adjList[node]) == 0 : #no where to go
                return False
            i = 0
            while i<len(adjList[node]):
                nextNode = adjList[node].pop(i)
                res.append(nextNode)
                if not dfs(nextNode):
                    res.pop()
                    adjList[node].insert(i,nextNode)
                else:
                    return True
            
            return False
            
                
        dfs("JFK")
        return res