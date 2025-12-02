order_list = input().strip()
board_list = [input().strip() for _ in range(2)]

order_len = len(order_list)
board_len = len(board_list[0])


def make_dp():
    # dp[다리길이][두루마리][악마천사]
    dp = [[[0] * 2 for _ in range(order_len)] for _ in range(board_len)]

    # 다리 길이
    for i in range(board_len):
        # 두루마리 길이
        for j in range(order_len):
            # 천사 악마 다리
            for k in range(2):
                # 두루마리 글자와 다리 글자 같을 때
                if board_list[k][i] == order_list[j]:
                    if j == 0:
                        dp[i][j][k] = 1
                    else:
                        # 다리길이
                        for l in range(i):
                            dp[i][j][k] += dp[l][j - 1][1 - k]
    return dp

def find_result(dp):
    result = 0
    for i in range(board_len):
        for j in range(2):
            result += dp[i][-1][j]
    return result


def solve():
    dp = make_dp()
    result = find_result(dp)
    print(result)


solve()
