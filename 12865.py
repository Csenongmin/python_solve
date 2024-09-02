import sys 
# 다이나믹 프로그래밍 아직 못풀었다
num, maxWeight = map(int, sys.stdin.readline().split())
element = []
dp = [0]*(maxWeight+1) # 0 헷갈리니까 쓰지 말기
for i in range(num):
    weight, value = map(int, sys.stdin.readline().split())
    element.append((weight, value))  # element[index][weight, value]
 
for elem in element:
    targetWeight = elem[0] # 가방 무게
    targetValue = elem[1]  # 가방 가치
    dpIndex = targetWeight # DP에서 쓸 인덱스
    if targetWeight > maxWeight: # 최대무게보다 큰건 고려 X
        continue
    #if targetValue > dp[targetWeight]: 조건? 넣으나마나 결과는 똑같은디
    if dp[dpIndex] == 0:
            dp[dpIndex] = targetValue
    elif dp[dpIndex] < targetValue:
         dp[dpIndex] = targetValue
    dpIndex+=1
    while dpIndex < maxWeight+1:
        if dp[dpIndex] == 0:
            dp[dpIndex] = targetValue
        elif (dp[dpIndex-targetWeight]+targetValue > dp[dpIndex]):
            dp[dpIndex] = dp[dpIndex-targetWeight]+targetValue
            targetValue = 0
        #dp[dpIndex] = max(dp[dpIndex-targetWeight]+targetValue, dp[dpIndex])
        dpIndex += 1
        
print(dp[maxWeight])