import random
import string

class Codec:
    def __init__(self):
        self.encode_map = {}
        self.decode_map = {}
        self.base_url = "http://tinyurl.com/"
        self.characters = string.ascii_letters + string.digits

    def encode(self, long_url: str) -> str:
        """Encodes a URL to a shortened URL."""
        if long_url in self.encode_map:
            return self.encode_map[long_url]

        tiny_url = self.generate_short_url()
        self.encode_map[long_url] = tiny_url
        self.decode_map[tiny_url] = long_url
        return tiny_url

    def decode(self, short_url: str) -> str:
        """Decodes a shortened URL to its original URL."""
        if short_url not in self.decode_map:
            raise ValueError("Invalid short URL")
        return self.decode_map[short_url]

    def generate_short_url(self) -> str:
        """Generates a unique short URL."""
        while True:
            tiny_url = self.base_url + self.generate_random_string()
            if tiny_url not in self.decode_map:
                return tiny_url

    def generate_random_string(self) -> str:
        """Generates a random string for the short URL."""
        return ''.join(random.choice(self.characters) for _ in range(6))