class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures)
        print(output)
        stack = []

        for i in range(len(temperatures)-1) :
            if temperatures[i+1] > temperatures[i] :
                output[i] = 1
                while stack and temperatures[i+1] > temperatures[stack[-1]] :
                    index = stack[-1]
                    output[index] = i+1 - stack.pop()
            else :
                stack.append(i)

        return output

