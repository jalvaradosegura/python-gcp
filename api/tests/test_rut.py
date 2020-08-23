import unittest

from ..rut_validator import rut_validator


class TestRut(unittest.TestCase):
    def test_rut_validator(self):
        """
        Test RUT with periods and hyphens
        """
        rut = '11.111.111-1'
        self.assertEqual(rut_validator(rut), True)

    def test_rut_validator_no_periods(self):
        """
        Test RUT with only hyphens
        """
        rut = '11111111-1'
        self.assertEqual(rut_validator(rut), True)

    def test_rut_validator_no_hyphen(self):
        """
        Test RUT with only periods
        """
        rut = '1.111.11111'
        self.assertEqual(rut_validator(rut), True)

    def test_rut_validator_no_periods_no_hyphen(self):
        """
        Test RUT with no periods and hyphens
        """
        rut = '111111111'
        self.assertEqual(rut_validator(rut), True)

    def test_rut_validator_wrong_one(self):
        """
        Test RUT with no check digit and a hyphen
        """
        rut = '11.111.111-'
        self.assertEqual(rut_validator(rut), False)

    def test_rut_validator_weird_characters(self):
        """
        Test RUT with a letter within it
        """
        rut = '11.11x.111-1'
        self.assertEqual(rut_validator(rut), False)

    def test_rut_validator_text_on_it(self):
        """
        Test RUT passing a word
        """
        rut = 'hello world'
        self.assertEqual(rut_validator(rut), False)

    def test_rut_validator_rut_with_k_lowercase(self):
        """
        Test RUT with a lowercase k as check digit
        """
        rut = '15.936.822-k'
        self.assertEqual(rut_validator(rut), True)

    def test_rut_validator_rut_with_k_uppercase(self):
        """
        Test RUT with an uppercase K as check digit
        """
        rut = '15.936.822-K'
        self.assertEqual(rut_validator(rut), True)

    def test_rut_validator_rut_with_k_uppercase_cleaned(self):
        """
        Test RUT with an uppercase K as check digit and no hyphens and periods
        """
        rut = '15936822K'
        self.assertEqual(rut_validator(rut), True)

    def test_rut_validator_rut_with_k_lowercase_cleaned(self):
        """
        Test RUT with a lowercase k as check digit and no hyphens and periods
        """
        rut = '15936822k'
        self.assertEqual(rut_validator(rut), True)
