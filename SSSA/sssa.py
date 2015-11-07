from SSSA.utils import utils

class sssa:
    prime = 115792089237316195423570985008687907853269984665640564039457584007913129639747
    util = utils()

    def create(self, minimum, shares, raw):
        if (shares < minimum):
            return

        secret = self.util.split_ints(raw)
        numbers = [0]
        polynomial = []
        for i in range(0, len(secret)):
            polynomial.append([secret[i]])
            for j in range(1, minimum):
                value = self.util.random()
                while value in numbers:
                    value = self.util.random()
                numbers.append(value)

                polynomial[i].append(value)

        result = [""]*shares

        for i in range(0, shares):
            for j in range(0, len(secret)):
                value = self.util.random()
                while value in numbers:
                    value = self.util.random()
                numbers.append(value)

                y = self.util.evaluate_polynomial(polynomial[j], value)

                result[i] += self.util.to_base64(value)
                result[i] += self.util.to_base64(y)

        return result

    def combine(self, shares):
        secrets = []

        for index,share in enumerate(shares):
            if len(share) % 88 != 0:
                return

            count = int(len(share) / 88)
            secrets.append([])

            for i in range(0, count):
                cshare = share[i*88:(i+1)*88]
                secrets[index].append([self.util.from_base64(cshare[0:44]), self.util.from_base64(cshare[44:88])])

        secret = [0] * len(secrets[0])

        for part_index,part in enumerate(secret):
            for share_index,share in enumerate(secrets):
                origin = share[part_index][0]
                originy = share[part_index][1]
                numerator = 1
                denominator = 1
                for product_index,product in enumerate(secrets):
                    if product_index != share_index:
                        current = product[part_index][0]
                        numerator = (numerator * (-1*current)) % self.util.prime
                        denominator = (denominator * (origin - current)) % self.util.prime

                working = ((originy * numerator * self.util.mod_inverse(denominator)) + self.util.prime)
                secret[part_index] = (secret[part_index] + working) % self.util.prime

        return self.util.merge_ints(secret)
