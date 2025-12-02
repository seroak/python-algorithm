n, m = map(int, input().split())
arr = list(map(int, input().split()))


def count_user(time):
    user = 0
    for use_time in arr:
        user += (time // use_time) + 1
    return user


# if n <= m:
#     print(n)
#     exit(0)
st = 0
en = (max(arr) * n) + 1
while st < en:
    mid = (st + en) // 2

    user = count_user(mid)
    if user < n:
        st = mid + 1
    else:
        en = mid

T = st
# print(T)
ago_user = count_user(T - 1)
# print(ago_user)
cur_user = n - ago_user
# print(cur_user)
flag = 0
for i in range(len(arr)):
    if T % arr[i] == 0:
        flag += 1
        if flag == cur_user:
            print(i + 1)
