nums = [1, 3, 5, 90, 56, 3]
target = 93

# def twoSum(nums: list[int], target: int) -> list[int]:
output = []
while not output:
    num1 = nums.pop()
    for idx2, num2 in enumerate(nums):
        if num1 + num2 == target:
            output = [len(nums), idx2]

print(output)