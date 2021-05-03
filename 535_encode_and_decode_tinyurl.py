import string 
letters = string.ascii_letters + string.digits
prefix = 'http://tinyurl.com/'
long2short = {}
short2long = {}
    
class Codec:
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in long2short:
            return prefix + long2short[longUrl]
        else:
            gen_letter = ''.join([letters[random.randint(0,61)] for i in range(6)])
            long2short[longUrl] = gen_letter
            short2long[gen_letter] = longUrl
            return prefix + gen_letter
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        short = shortUrl.split('/')[-1]
        if short in short2long:
            return short2long[short]
        else:
            return None
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))