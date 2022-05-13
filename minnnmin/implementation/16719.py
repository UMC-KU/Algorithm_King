def solution(string, start_idx):
    global copy, idx_list

    if start_idx in idx_list:
        return

    if "" not in copy[start_idx:]:
        return

    # 사전순 최선 찾기
    std_ch = 'a'
    std_idx = -1
    for idx, ch in enumerate(string):
        idx += start_idx
        if idx in idx_list:
            continue
        else:
            if ch < std_ch:
                std_ch = ch
                std_idx = idx
    copy[std_idx] = std_ch
    idx_list.append(std_idx)
    print(''.join(copy))
    solution(original[std_idx + 1:], std_idx + 1)

    # start_idx ~ std_idx 사이 부분 정렬
    solution(original[start_idx:std_idx], start_idx)

original = list(input())
n = len(original)
copy = [''] * n
idx_list = []
solution(original, 0)