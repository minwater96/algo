def solution(numbers, target):
    answer = 0

    def dfs(index, current_sum):
        if index == len(numbers):
            if current_sum == target:
                return 1
            else:
                return 0
        return dfs(index + 1, current_sum + numbers[index]) + dfs(index + 1, current_sum - numbers[index])
    
    # 처음에는 인덱스 0에서 시작하고, 현재 합은 0
    return dfs(0, 0)
        
    
    return answer