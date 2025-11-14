public class two_sum 
{
    public static int[] twoSum(int[] nums, int target) 
    {
        for (int n = 0; n < nums.length; n++)
        {
            for (int i = n + 1; i < nums.length; i++)
            {
                if (nums[n] + nums[i] == target)
                {
                    int [] result = {i,n};
                    return result;
                }
            }
        }
        return null;
    }

    public static void main(String[] args)
    {
        int [] nums = {3,2,4};
        System.out.println(twoSum(nums, 6));
    }
}

