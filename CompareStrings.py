from typing import List

def count_smallest_char(s):
    min_char = min(s)
    count = s.count(min_char)
    return count
                        

def compare_strings(str1: List[str], str2: List[str]) -> List[int]:
    str1_counts = []
    for s in str1: 
        count = count_smallest_char(s)
        str1_counts.append(count)

    result = []

    for s2 in str2:
        s2_count = count_smallest_char(s2)
        smaller_count = 0
        for s1_count in str1_counts:
            if s1_count < s2_count:
                smaller_count+=1
        result.append(smaller_count)
    
    return result

# Example usage
str1 = ["abcd", "aabc", "bd"]
str2 = ["aaa", "aa"]
print(compare_strings(str1, str2))  # Output: [3, 2]

# if __name__ == "__main__":
#     str1 = input().split()
#     str2 = input().split()
#     res = compare_strings(str1, str2)
#     print(" ".join(map(str, res)))