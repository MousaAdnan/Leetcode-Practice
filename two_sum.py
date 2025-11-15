def twoSum(nums, target):
    hash = {}
    for i in range(len(nums)):
        y = target - nums[i]
        if (y in hash):
            return ([i, hash[y]])
        else:
            hash[nums[i]] = i
        
def main():
    nums = [2,7,11,15]
    target = 9
    print(twoSum(nums, target))

if __name__ == "__main__":
    main()