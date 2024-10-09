class Solution: 
    def ValidateStackSequence(self, pushed, popped):
        stack = []
        x = 0
        y = 0

        while y < len(popped) and x < len(pushed):
            if pushed[x] != popped[y]:
                stack.append(pushed[0])
                x+=1
            else: 
                if x!= 0:
                    pushed.pop()
                    x-=1
                else: 
                    x+=1 
                y+=1
        
        if not stack: 
            return True 
        return False 


    
pushed = [1,2,3,4,5] 
popped = [4,5,3,2,1]
solution = Solution()
print(Solution.ValidateStackSequence())