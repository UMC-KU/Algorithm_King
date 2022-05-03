import sys

n = int(input())
words = set()
for w in range(n):
    words.add(sys.stdin.readline().rstrip())

words = list(words)
words.sort()
words.sort(key=lambda x:len(x))

for word in words:
    print(word)