n = int(input())
emp = list(map(int, input().split()))
node = [[] for _ in range(n)]
child_cnt = [0 for _ in range(n)]


def go(x):
    global child_cnt
    child_node = []
    # 리프 노드면 child_cnt에 0을 넣고 return
    if len(node[x]) == 0:
        child_cnt[x] = 0
        return
    else:
        for child in node[x]:
            go(child)
            # child_node에 child_cnt를 하나씩 넣어줌
            # child_cnt는 자식중 가장 높은 전달시간
            child_node.append(child_cnt[child])
        child_node.sort(reverse=True)
        # 가장 늦게 끝나는 자식부터 1씩 높여줌
        child_node = [child_node[i] + i + 1 for i in range(len(child_node))]

        child_cnt[x] = max(child_node)


for i in range(1, len(emp)):
    node[emp[i]].append(i)

go(0)
print(child_cnt)

