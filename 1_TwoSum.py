def twoSum(nums,target):
    for i in range(len(nums)):
        if target-nums[i] in nums:
            return [i,nums.index(target-nums[i])]
    return -1
if __name__ == "__main__":
    nums = [1,4,2,5,87,15]
    target = 20
    print(twoSum(nums,target))