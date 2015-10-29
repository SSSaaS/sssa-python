from random import SystemRandom

class utils:
    prime = 0

    def __init__(self, prime=115792089237316195423570985008687907853269984665640564039457584007913129639747):
        self.prime = prime

    def random(self):
        return SystemRandom().randrange(self.prime)

    def split_ints(self, secret):
        result = []

        for i in range(len(secret)/32 + 1):
            text =
