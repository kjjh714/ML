def solution(num_list):
    odd, even = 0, 0
    for i in range(len(num_list)):
        if (i%2 == 0):
            odd += num_list[i]
        else:
            even += num_list[i]
    if odd > even :
        answer = odd
    elif odd < even:
        answer = even
    else: answer = odd
    
    return answer