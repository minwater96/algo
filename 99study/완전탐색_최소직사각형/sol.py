def solution(sizes):
    answer = 0
    result = []
    answer1 = []
    answer2 = []

    for i in sizes:
        if i[0]>i[1]:
            i.append(i[0])
            i.pop(0)
            result.append(i)
        else:
            result.append(i)
    for num in result:
          answer1.append(num[0])
          answer2.append(num[1])
    
    answer = max(answer1) * max(answer2)

    return answer


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))	# => 4000
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))	# => 120
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))	# => 133