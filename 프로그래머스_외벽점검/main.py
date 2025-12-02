from itertools import permutations


def permutation(dist, limit):
    visited = [False] * len(dist)
    result = []

    def dfs(cur, limit, per):
        if cur == limit:
            result.append(per[:])
            return
        for i in range(len(dist)):
            if visited[i] is False:
                visited[i] = True
                per.append(dist[i])
                dfs(cur + 1, limit, per)
                per.pop()
                visited[i] = False

    dfs(0, limit, [])
    return result


def sol(n, weak, dist):
    weak_len = len(weak)
    for i in range(weak_len):
        weak.append(weak[i] + n)
    answer = len(dist) + 1
    print(weak)
    friends_list = permutation(dist, len(dist))
    print(friends_list)
    for start in range(weak_len):
        for friends in friends_list:
            count = 1
            position = weak[start] + friends[count - 1]
            for index in range(start, start + weak_len):
                # 친구가 지금 범위를 커버할 수 없을 때
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer
n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
print(sol(n, weak, dist))
