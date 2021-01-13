class Solution:
    """
    @param words: a list of words
    @param word1: a string
    @param word2: a string
    @return: the shortest distance between word1 and word2 in the list
    """
    def shortestDistanceII(self, words, word1, word2):
        # Write your code here
        from collections import defaultdict
        dictword = defaultdict(list)
        for i in range(len(words)):
            dictword[words[i]].append(i)

        list1 = dictword[word1]
        list2 = dictword[word2]
        i,j,dist = 0,0,float("inf")
        while i<len(list1) and j < len(list2):
            dist = min(dist, abs(list1[i] - list2[j]))
            if list1[i] < list2[j]:
                i+=1
            else:
                j+=1
        return dist

sol = Solution()
input =  ["practice", "makes", "perfect", "coding", "makes"]
print(sol.shortestDistanceII(input,"makes","practice"))