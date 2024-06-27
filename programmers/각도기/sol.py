def solution(angle):
    #예각 : 0 < angle < 90
    #직각 : angle = 90
    #둔각 : 90 < angle < 180
    #평각 : angle = 180
    answer = 0

    if 0< angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle < 180:
        return 3
    else:
        return 4

    return answer


print(solution(70)) #=> 1
print(solution(91)) #=> 3
print(solution(180)) #=> 4