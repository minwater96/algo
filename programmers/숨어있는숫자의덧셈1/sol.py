def solution(my_string):
    answer = 0

    # 풀이과정 1
    for char in my_string:
        if char.isdigit():
            answer += int(char)

    # 풀이과정 2
    for char in my_string:
        if ord('1') <= ord(char) <= ord('9'):
            answer += int(char)

    return answer


print(solution("aAb1B2cC34oOp")) # => 10
print(solution("1a2b3c4d123")) # => 16