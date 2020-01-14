# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:
import random

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        cnt = 0
        while cnt < 10:
            guess = wordlist[int(random.random()*len(wordlist))]
            cnt += 1
            tmp_list = []
            match_num = master.guess(guess)
            for w in wordlist:
                if self.match(guess, w) == match_num:
                    tmp_list.append(w)
            wordlist = tmp_list
    
    
    def match(self, a, b):
        res = 0
        for i in range(6):
            if a[i] == b[i]:
                res += 1
        return res