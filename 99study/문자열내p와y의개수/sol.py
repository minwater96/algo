def solution(s):
    s = s.lower()
    p_count = 0
    y_count = 0
    
    for char in s:
        if char == 'p':
            p_count += 1
        elif char == 'y':
            y_count += 1
    
    return p_count == y_count



print(solution("pPoooyY")) # => true
print(solution("Pyy"))	# => false