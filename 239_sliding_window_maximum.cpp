class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> res;
        multiset<int> st;
        for (int i = 0; i < nums.size(); i++){
            if (st.size() >= k) {
                // printf("%d, %d\n",i,nums[i-k]);
                st.erase(st.find(nums[i-k]));
            }
            // printf("%d st ", i);
            // for (std::multiset<int>::const_iterator j(st.begin()), end(st.end());j != end; ++j)
            //     printf("%d ", *j);
            // printf("\n");
            st.insert(nums[i]);
            if (i >= k-1)
                res.push_back(*st.rbegin());
        }
        return res;
    }
};