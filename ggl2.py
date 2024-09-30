def solution(A):
    moves = 0
    n = len(A)
    
    if n == 0:
        return 0
    
    for i in range(n):
        if i == 0:
            moves += A[i]
        elif A[i] > A[i-1]:
            moves += A[i] - A[i-1]

    return moves

A = [1,3,2,4,1]
print(solution(A)) 