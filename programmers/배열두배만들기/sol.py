def solution(numbers):
    
    answer = []
    for i in numbers:
        A = i * 2
        answer.append(A)
        
    return answer


print(solution([1, 2, 3, 4, 5])) # => [2, 4, 6, 8, 10]
print(solution([1, 2, 100, -99, 1, 2, 3])) # => [2, 4, 200, -198, 2, 4, 6]