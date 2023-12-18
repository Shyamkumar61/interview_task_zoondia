import random
import string


class UrlShortner:

    def __init__(self, token_size=None):
        self.token_size = token_size if token_size else 8
    
    def generate_url(self):
        letters = string.ascii_letters()
        actual_url = "".join(random.choice(letters) for _ in range(self.token_size))
        return actual_url