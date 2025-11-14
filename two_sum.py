def twoSum(nums, target):
    for n in range(len(nums)):
        for i in range(n, len(nums)):
            if(nums[n] + nums[i] == target):
                    return [n,i]
            
        
def main():
    nums = [2,7,11,15]
    target = 9
    print(twoSum(nums, target))

if __name__ == "__main__":
    main()