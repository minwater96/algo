def solution(n, k):
    answer = 0
    # n : 양꼬치 몇인분 / K : 음료수

    answer = (n * 12000) + (k * 2000) - (n//10*2000)

    return answer

    

