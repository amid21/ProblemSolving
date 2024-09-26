class Solution:
    def maximumEvenSplit(self, finalSum: int):
        # create an empty output set
        # tempSum = 0 
        # for loop (2, finalSum, 2)
        # tempSum += i
        # append i to list
        
        # if tempSum > finalSum 
        # remove from set finalSum - tempSum 
        # return set
        # elif tempSum == finalSum
        # return tempSum 
        if finalSum % 2 != 0:
            return []
        
        result = []
        current_even = 2
        
        # We will loop while the current_even is less than or equal to the remaining finalSum
        for _ in range(finalSum // 2):
            if finalSum < current_even:
                break
            result.append(current_even)
            finalSum -= current_even
            current_even += 2
        
        # If there's any leftover finalSum, add it to the last element
        if finalSum > 0:
            result[-1] += finalSum
        
        return result

solution = Solution()
print(solution.maximumEvenSplit(28))