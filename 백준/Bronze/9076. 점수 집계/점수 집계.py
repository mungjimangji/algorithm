T = int(input())
for _ in range(T):
    nums = list((map(int, input().split())))
    nums.sort()
    nums.pop(0)
    nums.pop()
    nums_sum = sum(nums)
    if nums[2] - nums[0] >= 4:
        print("KIN")
    else:
        print(nums_sum)