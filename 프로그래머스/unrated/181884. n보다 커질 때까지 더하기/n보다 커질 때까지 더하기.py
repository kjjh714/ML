def solution(numbers, n):
    
    temp = 0
    
    for i in numbers:
        temp += i
        if temp > n:
            answer = temp
            break
            
    return answer