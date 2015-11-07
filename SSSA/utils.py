import base64
import math
import struct
from random import SystemRandom

class utils:
    prime = 0

    def __init__(self, prime=115792089237316195423570985008687907853269984665640564039457584007913129639747):
        self.prime = prime

    def random(self):
        return SystemRandom().randrange(self.prime)

    def split_ints(self, secret):
        result = []

        for i in range(0, len(secret)/32 + 1):
            text = secret[i*32:(i+1)*32]
            text = text.encode('hex') + "00"*(32 - len(text))
            result.append(int(text, 16))

        return result

    def merge_ints(self, secrets):
        result = ""
        for index,secret in enumerate(secrets):
            if index == len(secrets)-1:
                working = ""
                secret_hex = hex(secret)[2:].replace("L", "")
                secret_hex = "0" * (64-len(secret_hex)) + secret_hex
                isnull = True
                for i in range(len(secret_hex)-2, -2, -2):
                    if secret_hex[i:i+2] == "00" and isnull == True:
                        pass
                    else:
                        isnull = False
                        working += chr(int(secret_hex[i:i+2], 16))
                result += working[::-1]
            else:
                working = ""
                secret_hex = hex(int(secret))[2:].replace("L", "")
                secret_hex = "0" * (64-len(secret_hex)) + secret_hex
                for i in range(len(secret_hex)-2, -2, -2):
                    working += chr(int(secret_hex[i:i+2], 16))
                result += working[::-1]
        return result

    def evaluate_polynomial(self, coefficients, value):
        result = 0
        for index,coefficient in enumerate(coefficients):
            result += coefficient*(value**index % self.prime)
            result = result % self.prime

        return result

    def to_base64(self, number):
        tmp = hex(number)[2:].replace("L", "")
        tmp = "0"*(len(tmp) % 2) + tmp
        return base64.urlsafe_b64encode('\00'*(64 - len(tmp)) + tmp.decode("hex"))

    def from_base64(self, number):
        return int(base64.urlsafe_b64decode(number).encode("hex"), 16)

    def gcd(self, a, b):
        if b == 0:
            return [a, 1, 0]
        else:
            n = int(math.floor(a*1.0/b))
            c = a % b
            r = self.gcd(b, c)
            return [r[0], r[2], r[1] - r[2]*n]

    def mod_inverse(self, number):
            remainder = (self.gcd(self.prime, number % self.prime))[2]
            if number < 0:
                remainder *= -1
            return (self.prime + remainder) % self.prime

