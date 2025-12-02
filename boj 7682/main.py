import sys


def check_win(player, board):
    """특정 플레이어가 이겼는지 확인하는 함수"""
    # 가로 3줄 확인
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
    # 세로 3줄 확인
    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True
    # 대각선 2줄 확인
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


while True:
    test_case = sys.stdin.readline().strip()
    if test_case == "end":
        break

    board = [list(test_case[i:i + 3]) for i in range(0, 9, 3)]

    x_count = test_case.count('X')
    o_count = test_case.count('O')

    # 1. X와 O의 개수 기본 조건 확인
    # O가 X보다 많거나, X가 O보다 2개 이상 많으면 불가능
    if not (x_count == o_count or x_count == o_count + 1):
        print("invalid")
        continue

    # 2. 누가 이겼는지 확인
    x_wins = check_win('X', board)
    o_wins = check_win('O', board)

    is_valid = False

    # 3. 경우에 따라 유효성 판단
    # Case 1: X가 이겼을 때
    if x_wins and not o_wins:
        # X가 이겼으므로 X가 마지막 수를 둔 것이어야 함
        if x_count == o_count + 1:
            is_valid = True

    # Case 2: O가 이겼을 때
    elif o_wins and not x_wins:
        # O가 이겼으므로 O가 마지막 수를 둔 것이어야 함
        if x_count == o_count:
            is_valid = True

    # Case 3: 아무도 이기지 못하고 게임이 끝났을 때 (무승부)
    elif not x_wins and not o_wins:
        # 무승부는 판이 꽉 찼을 때만 가능
        if test_case.count('.') == 0:
            is_valid = True

    # 위 모든 유효한 경우에 해당하지 않으면 invalid
    if is_valid:
        print("valid")
    else:
        print("invalid")