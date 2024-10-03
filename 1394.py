import sys
input = sys.stdin.readline

word = input().rstrip()
password = input().rstrip()
ans =  0
MOD = 900528
last_idx = len(password)-1
idx = 0

a = 0
for i in range(len(password)):
    idx = word.index(password[i])+1 #현재 문자 순서 
    if i > 0:  #전 부분도 계산 필요
        ans = (a*len(word))%MOD
    ans += idx %MOD
    a = ans
print(ans%MOD)
        


