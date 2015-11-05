import base64
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
        result = coefficients[0] % self.prime
        
        for index,coefficient in enumerate(coefficients):
            result += coefficient*(value**index % self.prime)
            result = result % self.prime

        return result

    def to_base64(self, number):
        tmp = hex(number)[2:].replace("L", "")
        return base64.urlsafe_b64encode('\00'*(64 - len(tmp)) + tmp.decode("hex"))

    def from_base64(self, number):
        return 
