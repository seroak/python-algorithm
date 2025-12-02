from collections import defaultdict, Counter

points = [[3, 2], [6, 4], [4, 7], [1, 4]]
routes = [[4, 2], [1, 3], [2, 4]]

def counter(obj):
    c = dict()
    for o in obj:
        if o not in c:
            c[o] = 0
        c[o] += 1
    return c
def solution(points, routes):
    answer = 0
    dic = defaultdict(list)

    for route in routes:
        time = 0
        for i in range(1, len(route)):
            x, y = points[route[i - 1] - 1][0], points[route[i - 1] - 1][1]
            target_x, target_y = points[route[i] - 1][0], points[route[i] - 1][1]

            if i == 1:
                dic[time].append((x, y))

            while x != target_x:
                if x < target_x:
                    x += 1
                else:
                    x -= 1
                time += 1
                dic[time].append((x, y))

            while y != target_y:
                if y < target_y:
                    y += 1
                else:
                    y -= 1
                time += 1
                dic[time].append((x, y))

    for key, items in dic.items():

        c = Counter(dic[key])

        for key in c:
            if c[key] > 1:
                answer += 1

    return answer


solution(points, routes)
