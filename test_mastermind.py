import unittest
from mastermind_classes import Key, Response
from mastermind import response

class TestMastermind(unittest.TestCase):
    def test_result(self):
        secret_key = Key(13527)
        guess = Key(34628)
        self.assertEqual(response(secret_key=secret_key, guess=guess), Response(21))

        secret_key = Key(15248)
        guess = Key(53267)
        self.assertEqual(response(secret_key=secret_key, guess=guess), Response(21))

        secret_key = Key(12462)
        guess = Key(53447)
        self.assertEqual(response(secret_key=secret_key, guess=guess), Response(2))

        secret_key = Key(32366)
        guess = Key(13458)
        self.assertEqual(response(secret_key=secret_key, guess=guess), Response(1))

        secret_key = Key(12136)
        guess = Key(41157)
        self.assertEqual(response(secret_key=secret_key, guess=guess), Response(21))


if __name__ == '__main__':
    unittest.main()
