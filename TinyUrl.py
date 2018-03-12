# Leetcode: https://leetcode.com/problems/encode-and-decode-tinyurl/description/

# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl 
# and it returns a short URL such as http://tinyurl.com/4e9iAk.

# Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode 
# algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be 
# decoded to the original URL.

import random

class Codec:
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    tinyUrl = "http://tinyurl.com/"
    keyMap = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        key = self.getKey()
        self.keyMap[key] = longUrl
        return self.tinyUrl + key

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        key = shortUrl.replace(self.tinyUrl, "")
        if key in self.keyMap:
            return self.keyMap[key]
    
    def getKey(self):
        key = self.generateKey()
        while key in self.keyMap:
            key = self.generateKey()
        
        return key
    def generateKey(self):
        key = ""
        for i in xrange(6):
            key += self.alphabet[random.randint(0, 61)]
        return key
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))