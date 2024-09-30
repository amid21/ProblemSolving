from typing import List
class Solution:
    def numSmallerByFrequency(self, queries, words):
        words_counter = []
        for w in words: 
            smallest_char = min(w)
            s_counter = w.count(smallest_char)
            words_counter.append(s_counter)
        result = []
        for q in queries: 
            smallest_char = min(q)
            q_counter = q.count(smallest_char)
            comparison_counter = 0 
            for w_counter in words_counter:
                if q_counter < w_counter:
                    comparison_counter+=1
            result.append(comparison_counter)
        
        return result


solution = Solution()
queries = ["bbb","cc"] 
words = ["a","aa","aaa","aaaa"]
result = solution.numSmallerByFrequency(queries, words) 
print(result)