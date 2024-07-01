def solution(n):
    answer = 0

    # 1. 문제풀이
    while n > 0:
        # a:몫, b:나머지
        a, b = divmod(n, 10)
        n = a

        answer += b

    # 2. 문제풀이 
    answer = sum(map(int, str(n)))

    # 3. 문제풀이
    for num in str(n):
        answer += int(num)

    return answer

print(solution(1234)) # => 10
print(solution(930211)) # => 16