import bisect 

def solution(A):
    # Return 0 if the array is empty
    if not A:
        return 0
    # Inititalize rows to 1, at lease one row
    rows = 1

    for i in range(1, len(A)):
        if A[i] > A[i-1]:
            # Increment rows whenever an element is greater than a previous
            rows += 1
    
    return rows

A = []
print(solution(A))
