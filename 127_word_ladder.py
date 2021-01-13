class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordlist_set = set(wordList)
        if endWord not in wordlist_set:
            return 0
        que = [beginWord]
        cnt = 1
        while len(que)!=0:
            for _ in range(len(que)):
                cur = que.pop(0)
                if cur == endWord:
                    return cnt
                for i in range(len(cur)):
                    for j in range(ord('a'),ord('z')+1):
                        tmp_char = cur[:i]+chr(j)+cur[i+1:]
                        if tmp_char in wordlist_set:
                            que.append(tmp_char)
                            wordlist_set.remove(tmp_char)
            cnt+=1
        return 0        
                        