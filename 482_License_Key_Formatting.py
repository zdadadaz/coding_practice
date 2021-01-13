class Solution:
    # string is License Key Formatting
    # O(N)
    # ord('a') = 97
    # chr(97) = 'a'
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        arr = []
        count = 0
        str_tmp = ''
        S = S.upper()
        for i in range(len(S)-1, -1, -1):
            if S[i] == "-":
                continue
            if count < K:
                str_tmp += S[i]
                count += 1
            if count == K:
                arr.append(str_tmp[::-1])
                count = 0
                str_tmp = ''
        if count < K and count >0:
            arr.append(str_tmp[::-1])
            
        out = ''
        for i in range(len(arr)-1,-1,-1):
            out += arr[i]
            out += "-"
            
        return out[:-1]