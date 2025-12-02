k, n, f = map(int, input().split())
relation = [[] for _ in range(n + 1)]
for _ in range(f):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)
answer = []


def find_friends(cur, friends):
    global answer
    # answer 에 뭔가 있으면 return
    # 즉 friends의 길이가 k랑 같아져서 answer에 배열을 넣어놓았을 때
    if answer:
        return
    if len(friends) == k:
        answer = sorted(friends)
        return
    # cur에서 하나 높은 걸 순회한다
    for i in range(cur + 1, n + 1):
        # 방문을 한적이 없어야한다
        if not visited[i]:
            # 지금까지 계속 누적하던 friends를 순회한다
            for num in friends:
                # relation을 set으로 만들어서 그 안에 있는 값이 없으면 break한다
                # 왜냐하면 친구로 전부 연결되어있어야하기 때문
                if num not in relation[i]:
                    break
            else:
                visited[i] = True
                find_friends(i, friends + [i])


for i in range(1, n + 1):
    visited = [False for _ in range(n + 1)]
    visited[i] = True
    find_friends(i, [i])
    if answer:
        break
if not answer:
    print(-1)
else:
    for ans in answer:
        print(ans)