import unittest

from ..rut_validator import rut_validator


class TestDateUtils(unittest.TestCase):
    def test_rut_validator(self):
        rut = '11.111.111-1'
        self.assertEqual(rut_validator(rut), True)

    def test_rut_validator_no_periods(self):
        rut = '11111111-1'
        self.assertEqual(rut_validator(rut), True)

    def test_rut_validator_no_hyphen(self):
        rut = '1.111.11111'
        self.assertEqual(rut_validator(rut), True)

    def test_rut_validator_no_periods_no_hyphen(self):
        rut = '111111111'
        self.assertEqual(rut_validator(rut), True)

    def test_rut_validator_wrong_one(self):
        rut = '11.111.111-'
        self.assertEqual(rut_validator(rut), False)

    def test_rut_validator_weird_characters(self):
        rut = '11.11x.111-1'
        self.assertEqual(rut_validator(rut), False)

    def test_rut_validator_text_on_it(self):
        rut = 'hello world'
        self.assertEqual(rut_validator(rut), False)

    def test_rut_validator_rut_with_k_lowercase(self):
        rut = '15.936.822-k'
        self.assertEqual(rut_validator(rut), True)

    def test_rut_validator_rut_with_k_uppercase(self):
        rut = '15.936.822-K'
        self.assertEqual(rut_validator(rut), True)

    def test_rut_validator_rut_with_k_uppercase_cleaned(self):
        rut = '15936822K'
        self.assertEqual(rut_validator(rut), True)

    def test_rut_validator_rut_with_k_lowercase_cleaned(self):
        rut = '15936822k'
        self.assertEqual(rut_validator(rut), True)
