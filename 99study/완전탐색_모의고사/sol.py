def solution(answers):
    #answer = []

    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    scores = [0, 0, 0]

    for idx, ans in enumerate(answers):
        if ans == a[idx%len(a)]:
            scores[0] += 1
        if ans == b[idx%len(b)]:
            scores[1] += 1
        if ans == c[idx%len(c)]:
            scores[2] += 1

    answer = []
    for idx, score in enumerate(scores):
        if score == max(scores):
            answer.append(idx+1)

    return answer



print(solution([1,2,3,4,5])) # => [1]
print(solution([1,3,2,4,2])) # => [1,2,3] 
