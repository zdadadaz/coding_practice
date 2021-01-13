class Solution:
    """
    @param words: a list of words
    @param word1: a string
    @param word2: a string
    @return: the shortest distance between word1 and word2 in the list
    """
    def shortestDistance(self, words, word1, word2):
        # Write your code here
        idx1 = -1
        idx2 = float('inf')
        minidx = float('inf')
        n = len(words)
        for i in range(len(words)):
            if words[i] == word1:
                idx1 = i
            if words[i] == word2:
                idx2 = i
            if -1 < idx1 < n and -1 < idx2 < n:
                if abs(idx1 - idx2) < minidx:
                    minidx = abs(idx1 - idx2)
        return minidx
                