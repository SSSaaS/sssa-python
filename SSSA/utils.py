import base64
import codecs
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

        working = None
        byte_object = None
        try:
            byte_object = bytes(secret, "utf8")
        except:
            byte_object = bytes(secret)
        text = str(codecs.encode(byte_object, 'hex_codec').decode('utf8')) + "00"*(32 - (len(byte_object) % 32))

        for i in range(0, int(len(text)/32)):
            result.append(int(text[i*32:(i+1)*32], 16))

        return result

    def merge_ints(self, secrets):
        result = ""
        for secret in secrets:
            hex_data = hex(secret)[2:].replace("L", "")
            hex_data = "0"*(len(hex_data) % 2) + hex_data
            result += "00"*(32 - len(hex_data)) + hex_data

        return str(codecs.decode(result, 'hex_codec').decode('utf8')).rstrip("\00\x00")

    def evaluate_polynomial(self, coefficients, value):
        result = 0
        for index,coefficient in enumerate(coefficients):
            result += coefficient*(value**index % self.prime)
            result = result % self.prime

        return result

    def to_base64(self, number):
        tmp = hex(number)[2:].replace("L", "")
        tmp = "0"*(len(tmp) % 2) + tmp

        try:
            tmp = bytes(tmp, "utf8")
        except:
            tmp = bytes(tmp)

        return str(base64.urlsafe_b64encode(b'\00'*(64 - len(tmp)) + codecs.decode(tmp, 'hex_codec')).decode('utf8'))

    def from_base64(self, number):
        tmp = base64.urlsafe_b64decode(number)
        try:
            tmp = bytes(tmp, "utf8")
        except:
            tmp = bytes(tmp)



        return int(codecs.encode(tmp, 'hex_codec'), 16)

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
