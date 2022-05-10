import sys

N, M = map(int, sys.stdin.readline().split())
DNA_list = [sys.stdin.readline().strip() for i in range(N)]

countA = [0]*M
countC = [0]*M
countG = [0]*M
countT = [0]*M

def count(dna_list):
    for dna in dna_list:
        for i, char in enumerate(dna):
            if char == 'A':
                countA[i] += 1
            elif char == 'C':
                countC[i] += 1
            elif char == 'G':
                countG[i] += 1
            else: # char == 'T'
                countT[i] += 1

def make_dna():
    result = []
    for a, c, g, t in zip(countA, countC, countG, countT):
        if max(a, c, g, t) == a:
            result.append('A')
        elif max(a, c, g, t) == c:
            result.append('C')
        elif max(a, c, g, t) == g:
            result.append('G')
        else:
            result.append('T')
    return ''.join(result)

def make_dist(dna_list, result):
    sum_of_dist = 0
    for dna in dna_list:
        for i, j in zip(dna, result):
            if i != j:
                sum_of_dist += 1
    print(sum_of_dist)

count(DNA_list)
result = make_dna()
print(result)
make_dist(DNA_list, result)