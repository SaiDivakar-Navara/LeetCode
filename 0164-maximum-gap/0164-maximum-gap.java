class Solution {
    public int maximumGap(int[] nums) {
        int maxdiff=Integer.MIN_VALUE;
        if(nums.length<2){
            return 0;
        }
        Arrays.sort(nums);
        for(int i=0;i<nums.length-1;i++){
            int diff=nums[i+1]-nums[i];
            if(diff>maxdiff){
                maxdiff=diff;
            }
        }
        return maxdiff;
    }
}