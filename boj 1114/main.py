l, k, c = map(int, input().split())
cuts = list(map(int, input().split()))
cuts = sorted(list(set(cuts)))
cuts.append(l)
k = len(cuts)
start = l // (k + 1)
end = l



def check(tgt):
    cut_count = c
    cut_from = l
    cut_idx = k - 1
    while cut_count > 0 and cut_idx >= 0:
        if cut_from - cuts[cut_idx] > tgt:
            if cuts[cut_idx + 1] - cuts[cut_idx] > tgt:
                return -1
            cut_count -= 1
            cut_from = cuts[cut_idx + 1]
        cut_idx -= 1
    if cut_count > 0:
        cut_from = cuts[0]
    if cut_from > tgt:
        return -1
    else:
        return cut_from


while start < end:
    mid = (start + end) // 2
    ret = check(mid)
    if ret >= 1:
        end = mid

    else:
        start = mid + 1
print(start, check(start))
