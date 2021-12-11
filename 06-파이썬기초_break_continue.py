num = 0
while True: # while True : 무한 루프
    num += 1
    if num % 2 == 1: # num이 홀수라면?
        continue # 반복문 처음으로 돌려 보냄
    print(num)
    if num == 20: # == : 양쪽 값이 같냐?
        break # 반복문을 강제 탈출 시킴