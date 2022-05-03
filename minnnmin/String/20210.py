import sys
from functools import cmp_to_key

alphaDict = {'A': 1, 'a': 2, 'B': 3, 'b': 4, 'C': 5, 'c': 6, 'D':7, 'd': 8, 'E': 9, 'e': 10, 'F': 11, 'f': 12, 'G': 13, 'g': 14, 'H': 15, 'h': 16, 'I': 17, 'i': 18, 'J': 19, 'j': 20, 'K': 21, 'k': 22, 'L': 23, 'l': 24, 'M': 25, 'm': 26, 'N': 27, 'n': 28, 'O': 29, 'o': 30, 'P': 31, 'p': 32, 'Q': 33, 'q': 34, 'R': 35, 'r':36, 'S': 37, 's': 38, 'T': 39, 't': 40, 'U': 41, 'u': 42, 'V': 43, 'v': 44, 'W': 45, 'w': 46, 'X': 47, 'x': 48, 'Y': 49, 'y': 50, 'Z': 51, 'z': 52}

def parse_filename(filename):
    result = []
    tmp = filename[0]
    if filename[0].isalpha():
        ex_type = 'alpha'
    else:
        ex_type = 'digit'

    for char in filename[1:]:
        if char.isalpha():
            type = 'alpha'
        else:
            type = 'digit'

        if ex_type == type:
            tmp += char
        else:
            result.append(tmp)
            tmp = char
            ex_type = type
    result.append(tmp)
    return result

def compare(file_x, file_y):
    for i in range(min(len(file_x), len(file_y))):
        if file_x[i].isalpha() and file_y[i].isalpha():
            if file_x[i] == file_y[i]:
                continue
            else:
                for j in range(min(len(file_x[i]), len(file_y[i]))):
                    if alphaDict[file_x[i][j]] < alphaDict[file_y[i][j]]:
                        return 1
                    elif alphaDict[file_x[i][j]] > alphaDict[file_y[i][j]]:
                        return -1
                    else:
                        continue
                if len(file_x[i]) < len(file_y[i]):
                    return 1
                else:
                    return -1
        elif file_x[i].isdigit() and file_y[i].isdigit():
            if file_x[i] == file_y[i]:
                continue
            elif int(file_x[i]) == int(file_y[i]): # ex) 001 vs 0001
                if len(file_x[i]) < len(file_y[i]):
                    return 1
                else:
                    return -1
            elif int(file_x[i]) < int(file_y[i]):
                return 1
            else:
                return -1
        elif file_x[i].isalpha() and file_y[i].isdigit():
            return -1
        else: # file_x[i].isdigit() and file_y[i].isalpha():
            return 1

    if len(file_x) < len(file_y):
        return 1
    else:
        return -1

n = int(input())
original_filenames = [] # ['Foo123Bar', ...]
parsed_filenames = []   # [['Foo', '123', 'Bar'], [...] ...]
for _ in range(n):
    filename = sys.stdin.readline().rstrip()
    original_filenames.append(filename)
    parsed_filenames.append(parse_filename(filename))
answer = sorted(parsed_filenames, key= cmp_to_key(compare), reverse=True)

for val in answer:
    print("".join(val))