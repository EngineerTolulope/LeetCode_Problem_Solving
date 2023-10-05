class Codec:
    def __init__(self):
        self.encode_map, self.decode_map = {}, {}
        self.base_url = "http://tinyurl.com/"


    def encode(self, long_url: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        tiny_url = self.base_url + str(len(self.encode_map) + 1)
        self.encode_map[long_url] = tiny_url
        self.decode_map[tiny_url] = long_url
        return tiny_url

        

    def decode(self, short_url: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decode_map[short_url]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))