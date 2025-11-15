def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    
    used = set ()
    for i in range(len(nums)):
        if (nums[i] in used):
            return True
        
        used.add(nums[i])
    return False

def main():
    nums = [1,2,3,1]
    print(containsDuplicate(nums))

if __name__ == "__main__":
    main()