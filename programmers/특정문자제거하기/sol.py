def solution(my_string, letter):
    answer = ''

    # 1. 풀이방법
    answer = my_string.replace(letter, '')

    # 2. 풀이방법
    for char in my_string:
        if char != letter:
            answer += char


    return answer




print(solution("abcdef", "f")) # => "abcde"
print(solution("BCBdbe", "B")) # => "Cdbe"