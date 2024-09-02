import sys
input = sys.stdin.readline

key = list(input().rstrip())
password = list(input().rstrip())

ans=0
mod = 900528
len_key = len(key)
len_password = len(password)

j = 0
for elem in password:
    index = word.index(elem)  # 암호 집합에서의 위치
    if j < length_password-1:   # 전의 경우의수 합
        ans += length_word ** (j + 1) 
    
    if password.index(elem) == length_password - 1:  # 정답 암호중 마지막 암호
        ans += index+1
    else: 
        ans += length_word ** index * index
    j += 1

print(ans % 900528)
