class Solution
{
public:
    int hIndex(vector<int> &citations)
    {
        sort(citations.begin(), citations.end());
        int n = citations.size(), i = 1;
        for (i; i <= n; i++)
        {
            if (citations[n - i] < i)
                break;
        }
        return i - 1;
    }
};