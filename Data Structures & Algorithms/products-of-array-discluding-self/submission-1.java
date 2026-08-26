class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] forw = new int[nums.length];
        int[] rev = new int[nums.length];
        forw[0] = nums[0];
        for(int i = 1; i < nums.length; i++) 
            forw[i] = forw[i-1] * nums[i];

        rev[rev.length - 1] = nums[nums.length - 1];
        for(int i = nums.length - 2; i >= 0; i--) 
            rev[i] = rev[i+1] * nums[i];

        int[] ret = new int[nums.length];
        ret[0] = rev[1];
        ret[ret.length - 1] = forw[forw.length - 2];
        for(int i = 1; i < nums.length - 1; i++) {
            ret[i] = rev[i+1] * forw[i-1];
        }

        return ret;

    }
}  
