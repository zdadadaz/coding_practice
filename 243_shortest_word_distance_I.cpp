class Solution
{
public:
    /**
     * @param words: a list of words
     * @param word1: a string
     * @param word2: a string
     * @return: the shortest distance between word1 and word2 in the list
     */
    int shortestDistance(vector<string> &words, string &word1, string &word2)
    {
        // Write your code here
        int idx1 = -1, idx2 = -1, minidx = INT_MAX, n = words.size();
        for (int i = 0; i < n; i++)
        {
            if (!words[i].compare(word1))
                idx1 = i;
            if (!words[i].compare(word2))
                idx2 = i;
            if ((0 <= idx1 && idx1 < n) && (0 <= idx2 && idx2 < n) && (std::abs(idx1 - idx2) < minidx))
                minidx = abs(idx1 - idx2);
        }
        return minidx;
    }
};