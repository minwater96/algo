def solution(n):
    arr = list(str(n))
    arr.reverse()
    
    return list(map(int, arr))

print(solution(12345)) # => [5,4,3,2,1]