from django.test import TestCase
from .helpers import check_valid


class TestCardValider(TestCase):

    def test_first_line_between_1_and_100(self):
        """First line should be greater > 0 and <= 100."""
        str_file = """6\n4123456789123456\n5123-4567-8912-3456\n61234-567-8912-3456\n4123356789123456\n5133-3367-8912-3456\n5123 - 3567 - 8912 - 3456\n"""
        for line in str_file.splitlines():
            self.assertTrue(int(line[0]) > 0)
            self.assertTrue(int(line[0]) <= 100)

    def test_invalid(self):
        """Should receive Invalid to all numbers in the list."""
        invalids = [
            '61234-567-8912-3456',
            '5123 - 3567 - 8912 - 3456',
            '5133-3367-8912-3456',
            '5133-3367-8912-345X',
            '42536258796157867',
            '4424444424442444',
            '5122-2368-7954 - 3214',
            '44244x4424442444',
            '0525362587961578',
        ]
        for invalid in invalids:
            self.assertEqual('Invalid', check_valid(invalid))

    def test_valid(self):
        """Should receive Valid to all numbers in the list."""
        valids = [
            '4424424424442444',
            '5122-2368-7954-3214',
            '4123456789123456',
            '5123-4567-8912-3456',
            '4123356789123456',
        ]
        for valid in valids:
            self.assertEqual('Valid', check_valid(valid))
