class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid, n = len(s)//2, len(s)
        m1 = Counter(s[:mid].lower())
        m2 = Counter(s[mid:].lower())
        vowels = ['a','e','i','o','u']
        cnt1=cnt2 = 0
        for v in vowels:
            cnt1 += m1[v]
            cnt2 += m2[v]
        return True if cnt1 == cnt2 else False

    def halvesAreAlike_noextraspace(self, s: str) -> bool:
        mid, n = len(s)//2, len(s)
        vowels = ['a','e','i','o','u']
        def cntvowel(arr):
            cnt = 0
            for i in arr:
                if i in vowels:
                    cnt +=1
            return cnt
        return True if cntvowel(s[:mid].lower())==cntvowel(s[mid:].lower()) else False