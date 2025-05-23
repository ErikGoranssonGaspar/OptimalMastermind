import unittest
from mastermind import GuessOutcome, Key, Response, response

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


    def test_GuessOutcume_compatible_with(self):
        guess_outcome = GuessOutcome(guess=Key(53267), response=Response(21))
        self.assertTrue(guess_outcome.compatible_with(Key(15248)))
        self.assertFalse(guess_outcome.compatible_with(Key(15348)))

        guess_outcome = GuessOutcome(guess=Key(53447), response=Response(2))
        self.assertTrue(guess_outcome.compatible_with(Key(12462)))
        self.assertFalse(guess_outcome.compatible_with(Key(35128)))

        guess_outcome = GuessOutcome(guess=Key(13458), response=Response(1))
        self.assertTrue(guess_outcome.compatible_with(Key(32366)))
        self.assertFalse(guess_outcome.compatible_with(Key(34346)))

        guess_outcome = GuessOutcome(guess=Key(41157), response=Response(21))
        self.assertTrue(guess_outcome.compatible_with(Key(12136)))
        self.assertFalse(guess_outcome.compatible_with(Key(22346)))

if __name__ == '__main__':
    unittest.main()
