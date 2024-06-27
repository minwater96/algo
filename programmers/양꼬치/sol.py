def solution(n, k):
    answer = 0
    # n : 양꼬치 몇인분 / K : 음료수

    food_price = n * 12000
    
    if n > 10:
        service = n // 10
        drink_price = (k - service) * 2000
    else:
        drink_price = k * 2000

    return food_price + drink_price

print(solution(10, 3)) # => 124,000
print(solution(64, 6)) # => 768,000