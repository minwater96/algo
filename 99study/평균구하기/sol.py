def solution(arr):
    answer = 0
    result = 0

    for i in arr:
        result += i
        answer = result / len(arr)

    return answer


print(solution([1,2,3,4]))	# => 2.5
print(solution([5,5]))	# => 5