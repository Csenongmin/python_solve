import sys
input = sys.stdin.readline
color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

d = {}
for i in range(10):
    d[color[i]] = i

ohm = [input().rstrip() for _ in range(3)]
print((d[ohm[0]] * 10 + d[ohm[1]]) * 10**d[ohm[2]])
