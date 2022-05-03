import sys

origin_list = list(sys.stdin.readline().rstrip())
tmp_idx = []
tmp_word = []
is_word = True
for i in range(len(origin_list)):
    if origin_list[i] == '<':
        if tmp_idx:
            tmp_idx.reverse()
            for idx, char in zip(tmp_idx, tmp_word):
                origin_list[idx] = char
            tmp_idx.clear()
            tmp_word.clear()
        is_word = False
        continue
    if is_word == False and origin_list[i] == '>':
        is_word = True
        continue
    if origin_list[i] == ' ':
        if tmp_idx:
            tmp_idx.reverse()
            for idx, char in zip(tmp_idx, tmp_word):
                origin_list[idx] = char
            tmp_idx.clear()
            tmp_word.clear()
        continue
    if is_word and origin_list[i] != ' ':
        tmp_idx.append(i)
        tmp_word.append(origin_list[i])

if tmp_idx:
    tmp_idx.reverse()
    for idx, char in zip(tmp_idx, tmp_word):
        origin_list[idx] = char

print(''.join(origin_list))