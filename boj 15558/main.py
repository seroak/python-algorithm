# from collections import deque
#
# n, k = map(int, input().split())
# left = list(map(int, input().rstrip()))
# right = list(map(int, input().rstrip()))
# lines = [left, right]
# left_vis = [False] * n
# right_vis = [False] * n
# lines_vis = [left_vis, right_vis]
#
# lines_vis[0][0]= True
# def sol():
#     # [시간, 왼쪽인지 오른쪽인지, 위치]
#     queue = deque()
#     queue.append([0, 0, 0])
#     while queue:
#         run_away = len(queue)
#         for _ in range(run_away):
#             time, dist, loc = queue.popleft()
#             if loc + 1 >= n or loc + k >= n:
#                 return 1
#
#             if loc + 1 >= time + 1 and lines[dist][loc + 1] == 1 and lines_vis[dist][loc + 1] is False:
#                 lines_vis[dist][loc + 1] = True
#                 queue.append([time + 1, dist, loc + 1])
#             if loc - 1 >= 0 and loc - 1 >= time + 1 and lines[dist][loc - 1] == 1 and lines_vis[dist][loc - 1] is False:
#
#                 lines_vis[dist][loc - 1] = True
#                 queue.append([time + 1, dist, loc - 1])
#             if loc + k >= time + 1 and lines[(dist+1) % 2][loc + k] == 1 and lines_vis[(dist+1) % 2][loc + k] is False:
#                 lines_vis[(dist + 1) % 2][loc + k] = True
#                 queue.append([time + 1, (dist + 1) % 2, loc + k])
#     return 0
#
# print(sol())
arr = [1,2,3,4]
arr.insert(3,1)
print(arr)