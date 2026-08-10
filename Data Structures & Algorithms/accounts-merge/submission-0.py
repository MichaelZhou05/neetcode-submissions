class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        #email is the node
        # unifion find emails given accounts
        parents = []
        emailToIndex = {}
        indexToEmail = defaultdict(str)
        index = 0
        emailToName = defaultdict(str)
        for account in accounts:
            name = account[0]
            for i in range(1,len(account)):
                email = account[i]
                emailToName[email] = name
                if email in emailToIndex: continue
                emailToIndex[email] = index
                indexToEmail[index] = email
                parents.append(index)
                index += 1

        def find(index):
            if parents[index] == index :
                return index
            
            parent = find(parents[index])
            parents[index] = parent
            return parent
        
        def union(a,b):
            if a == b : return
            parentA,parentB = find(a),find(b)
            parents[parentB] = parentA
            return parentA 
        

        for account in accounts:
            firstEmail = account[1]
            for i in range(1,len(account)):
                parent = union(emailToIndex[account[i]],emailToIndex[firstEmail])
        
        parentEmailMap = defaultdict(set)
        for account in accounts:
            for i in range(1,len(account)):
                parent = find(emailToIndex[account[i]])
                parentEmail = indexToEmail[parent]
                parentEmailMap[parentEmail].add(account[i])
        
        ret = []
        for parentEmail in parentEmailMap:
            temp = []
            temp.append(emailToName[parentEmail])
            arr = list(parentEmailMap[parentEmail])
            arr.sort()
            temp = temp + arr
            ret.append(temp)




        
        return ret

