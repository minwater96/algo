def solution(participant, completion):
    name_count = {}
    
    # 참가자 이름을 딕셔너리에 카운트
    for name in participant:
        if name in name_count:
            name_count[name] += 1
        else:
            name_count[name] = 1
    
    # 완주자 이름으로 카운트 감소
    for name in completion:
        name_count[name] -= 1
    
    # 카운트가 0 이상인 이름 찾기
    for name in name_count:
        if name_count[name] > 0:
            return name


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))	#=> "leo"
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])) # => "vinko"
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])) # => "mislav"