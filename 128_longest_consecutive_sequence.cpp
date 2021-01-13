class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::unordered_set<int> myset;
        int maxlen = 0;
        for(int i =0; i<nums.size();i++)
            myset.insert(nums[i]);
        for(int i =0; i<nums.size();i++)
        {
            if (myset.find(nums[i]-1) == myset.end() && myset.find(nums[i]) != myset.end() && myset.find(nums[i]+1) != myset.end()){
                int count=1, start = nums[i];
                for (start; count < nums.size() && myset.find(start+1) != myset.end(); start++)
                    count++;
                maxlen = std::max(maxlen, count);
            }
        }
        if (myset.size()>0 && maxlen==0)
            return 1;
        else
            return maxlen;
    }
};