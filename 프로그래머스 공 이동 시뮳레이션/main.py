def solution(n, m, x, y, queries):
    sr, sc, er, ec = x, y, x, y  # 시작 행/열, 끝 행/열 (목적지 범위)

    for d, dx in reversed(queries):
        if d == 0:
            if sc == 0:
                ec = min(m-1, ec + dx)
            else:
                sc = min(m-1, sc + dx)
                ec = min(m-1, ec + dx)
        elif d == 1:
            if ec == m - 1:
                sc = max(0, sc - dx)
            else:
                sc = max(0, sc - dx)
                ec = max(0, ec - dx)
        elif d == 2:
            if sr == 0:
                er = min(n-1, er + dx)
            else:
                sr = min(n-1, sr + dx)
                er = min(n-1, er + dx)
        else:
            if er == n-1:
                sr = max(0, sr - dx)
            else:
                sr = max(0, sr - dx)
                er = max(0, er - dx)
        if sr > er or sc > ec:
            return 0
    return (er - sr + 1) * (ec - sc + 1)

n = 5
m = 5
x = 1
y = 4
queries = [[1, 4],[1,3]]
print(solution(n, m, x, y, queries))
n = 5
m = 5
x = 1
y = 4
queries = [[1, 4],[1,3]]
print(solution(n, m, x, y, queries))