class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n=nums.size();
        int left=0;
        int right=n-1;
        while(left<=right)
        {
            int mid=(left+right)/2;
            if(nums[mid]==target)
            return mid;
            //left
           if(nums[mid]>=nums[left])
            {
                if( target>=nums[left] && target<=nums[mid])
                {
                    right= mid-1;

                }
                else left=mid+1;
            }
            //right sorted
                else
                {
                    if(target>=nums[mid] && target<=nums[right])
                    {
                        left = mid+1;

                    }
                    else right =mid -1;
                }
            
                               

        }
                                         return -1;
  
 
    }
};