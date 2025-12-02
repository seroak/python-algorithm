def solution(numbers):
    answer = []
    for num in numbers:
        # 수를 이진수로 변경
        b = bin(num)[2:]
        # 이진수의 길이에 1을 더하고 이진수로 변경
        node_len_bin = bin(len(b) + 1)[2:]
        print(len(b))
        # [1:]여기에 1이 있으면 포화 이진트리의 길이가 아님
        if '1' in node_len_bin[1:]:
            dummies = (1 << len(node_len_bin)) - len(b)
            b = "0" * dummies + b
        print(b)
    return answer


numbers = [7, 42, 5, 32]
solution(numbers)
