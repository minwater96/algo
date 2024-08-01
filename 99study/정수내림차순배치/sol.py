def solution(n):
    answer = 0
    answer = str(n)

    answer = sorted(answer, reverse=True)
    result= (''.join(answer))
    return int(result)

print(solution(118372)) #=>	873211