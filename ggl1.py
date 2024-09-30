from itertools import combinations

def solution(digits):
    max_number = 0 
    # Try all possible combinations of 1-3 digits
    for r in range(1, 4):
        for c in combinations(digits, r):
            num = int(''.join(map(str, c))) # Convert the combination into an int number
            max_number = max(max_number, num) # Update max_number if we find a larger one
    return max_number

digits = [0,0,0,1]
print(solution(digits))