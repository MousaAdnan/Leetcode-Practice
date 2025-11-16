
def missingNumber(nums):
    s = set(nums)

    for i in range(len(nums) + 1):
        if (i in s):
            continue
        return i


def main():
    nums = [0,1]
    print(missingNumber(nums))

if __name__ == "__main__":
    main()