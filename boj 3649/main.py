while True:
    try:
        x = int(input())
        n = int(input())
        arr = list()
        for _ in range(n):
            num = int(input())
            arr.append(num)
        arr.sort()
        st = 0
        en = len(arr) - 1
        while st < en:
            if arr[st] + arr[en] == x * 10000000:
                print("yes", arr[st], arr[en])
                break
            elif arr[st] + arr[en] < x * 10000000:
                st += 1
            else:
                en -= 1
        else:
            print("danger")
    except:
        break
