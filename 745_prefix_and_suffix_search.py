class WordFilter:

    def __init__(self, words: List[str]):
        self.m = {}
        for idx, w in enumerate(words):
            n = len(w)
            prefixes = ['']*(n+1)
            suffixes = ['']*(n+1)
            # list all prefix and suffix
            for i in range(n):
                prefixes[i+1] = prefixes[i] + w[i]
                suffixes[i+1] = w[n-i-1] + suffixes[i]
            # all combination of prefix and suffix for keys
            for i in prefixes:
                for j in suffixes:
                    self.m[i+'_'+j] = idx
    def f(self, prefix: str, suffix: str) -> int:
        key = prefix + '_' + suffix
        return self.m[key] if key in self.m else -1

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)