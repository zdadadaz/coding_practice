class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        self.m = {}
        for idx, i in enumerate(order):
            self.m[i] = idx
        return self.mergesort(words, 0, len(words)-1)
        
    def mergesort(self, words, l,r):
        if l >=r :
            return True
        mid = (l+r)//2
        res = True
        res &= self.mergesort(words, l, mid)
        res &= self.mergesort(words, mid+1, r)
        res &= self.check_words_order(words[l:mid+1], words[mid+1:r+1])
        return res
    
    def check_words_order(self, arr1, arr2):
        n1, n2 = len(arr1), len(arr2)
        i=j=0
        while i < n1 or j < n2:
            w1 = arr1[i] if i < n1 else arr1[-1]
            w2 = arr2[j] if j < n2 else arr2[-1]
            if not self.check_word_order(w1, w2):
                return False
            i+=1
            j+=1
        return True
    
    def check_word_order(self, w1, w2):
        k=p=0
        n1,n2 = len(w1), len(w2)
        while k < n1 and p < n2:
            if w1[k]==w2[p]:
                k+=1
                p+=1
                continue
            if self.m[w1[k]]>self.m[w2[p]]:
                return False
            else:
                return True
        if p==n2 and k < n1:
            return False
        return True
            

    def isAlienSorted_intuition(self, words: List[str], order: str) -> bool:
        m = {}
        for idx, i in enumerate(order):
            m[i] = idx
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return False # for case apple, app
                if words[i][j] != words[i+1][j]:
                    if m[words[i][j]]> m[words[i+1][j]]:
                        return False
                    break
        return True