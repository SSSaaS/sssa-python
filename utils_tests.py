# -*- coding: utf8 -*-

import unittest
from SSSA import utils

class TestStringMethods(unittest.TestCase):
    def test_random(self):
        util = utils()
        for i in range(0, 10000):
            self.assertEqual(util.random() < util.prime, True)

    def test_base_conversion(self):
        util = utils()
        for i in range(0, 10000):
            value = util.random()
            self.assertEqual(util.from_base64(util.to_base64(value)), value)

    def test_to_base64(self):
        util = utils()
        for i in range(0, 10000):
            value = util.random()
            self.assertEqual(len(util.to_base64(value)), 44)

    def test_split_merge(self):
        util = utils()
        values = ["N17FigASkL6p1EOgJhRaIquQLGvYV0", "0y10VAfmyH7GLQY6QccCSLKJi8iFgpcSBTLyYOGbiYPqOpStAf1OYuzEBzZR", "KjRHO1nHmIDidf6fKvsiXWcTqNYo2U9U8juO94EHXVqgearRISTQe0zAjkeUYYBvtcB8VWzZHYm6ktMlhOXXCfRFhbJzBUsXaHb5UDQAvs2GKy6yq0mnp8gCj98ksDlUultqygybYyHvjqR7D7EAWIKPKUVz4of8OzSjZlYg7YtCUMYhwQDryESiYabFID1PKBfKn5WSGgJBIsDw5g2HB2AqC1r3K8GboDN616Swo6qjvSFbseeETCYDB3ikS7uiK67ErIULNqVjf7IKoOaooEhQACmZ5HdWpr34tstg18rO"]
        for value in values:
            self.assertEqual(util.merge_ints(util.split_ints(value)), value)

    def test_split_merge_odds(self):
        util = utils()
        values = ["a" + "\0"*100 + "a", "a"*31 + "哈囉世界", "こんにちは、世界"*32]
        for value in values:
            self.assertEqual(util.merge_ints(util.split_ints(value)), value)

    def test_mod_inverse(self):
        util = utils()
        for i in range(0, 10000):
            value = util.random()
            self.assertEqual((value * util.mod_inverse(value)) % util.prime, 1)

    def test_evaluate_polynomial(self):
        util = utils()
        values = [[[20, 21, 42], 0], [[0, 0, 0], 4], [[1, 2, 3, 4, 5], 10]]
        results = [20, 0, 54321]
        for index,value in enumerate(values):
            self.assertEqual(util.evaluate_polynomial(value[0], value[1]), results[index])

if __name__ == '__main__':
    unittest.main()
