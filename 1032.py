import sys
input = sys.stdin.readline

N = int(input().rstrip())
files = sorted([input().strip() for _ in range(N)])
ans = files[0]

for f in files:
    if f == ans:
        continue
    else:
        for i in range(len(f)):
            if ans[i] != f[i]:
                ans = ans[:i] + '?' + ans[i+1:]
        
print(ans)