# Link: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000051060/00000000000588f4

def solve(a, b):
    m = (a + b) // 2
    print(m)
    s = input()
    if s == "CORRECT":
        return
    elif s == "TOO_SMALL":
        a = m + 1
    else:
        b = m - 1
    solve(a, b)

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    _ = int(input())
    solve(a + 1, b)