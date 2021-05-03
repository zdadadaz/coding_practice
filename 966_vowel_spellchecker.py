class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def replace_vowl(w):
            w = w.replace('a','_')
            w = w.replace('e','_')
            w = w.replace('i','_')
            w = w.replace('o','_')
            w = w.replace('u','_')
            return w
        org_m = set(wordlist)
        small_m = {}
        for idx,w in enumerate(wordlist):
            if w.lower() not in small_m:
                small_m[w.lower()] = idx
        
        noVow_m = {}
        for idx,w in enumerate(wordlist):
            w = replace_vowl(w.lower())
            if w not in noVow_m:
                noVow_m[w] = idx
        res = []
        for q in queries:
            if q in org_m:
                # print('all the same', q)
                res.append(q)
            elif q.lower() in small_m:
                # print('lower the same', q.lower)
                res.append(wordlist[small_m[q.lower()]])
            else:
                noVow_q = replace_vowl(q.lower())
                if noVow_q in noVow_m:
                    # print('no vowl the same', noVow_q)
                    res.append(wordlist[noVow_m[noVow_q]])
                else:
                    res.append('')
        return res

class Solution_sameIdea_leanCode(object):
    def spellchecker(self, wordlist, queries):
        # or re.sub(r'aeiou', '*', word)
        def devowel(word):
            return "".join('*' if c in 'aeiou' else c
                           for c in word)

        words_perfect = set(wordlist)
        words_cap = {}
        words_vow = {}

        for word in wordlist:
            wordlow = word.lower()
            words_cap.setdefault(wordlow, word) # store the first lower capital character only
            words_vow.setdefault(devowel(wordlow), word) # store the first lower capital and no vowl character only

        def solve(query):
            if query in words_perfect:
                return query

            queryL = query.lower()
            if queryL in words_cap:
                return words_cap[queryL]

            queryLV = devowel(queryL)
            if queryLV in words_vow:
                return words_vow[queryLV]
            return ""

        # for loop function and list
        return map(solve, queries)
            