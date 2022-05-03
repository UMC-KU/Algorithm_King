n = int(input())
nums = input()
nums = nums.replace('0', '')
num_list = list(nums)

sum = 0
for i in num_list:
    sum += int(i)

print(sum)