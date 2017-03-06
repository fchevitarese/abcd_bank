import re


class CreditCard(object):
    def __init__(self, number, *args, **kwargs):
        self.number = number

        super(CreditCard, self).__init__()

    def check_valid(self):
        """Check if the number is valid following patterns.
        ► It must start with a 4, 5 or 6.
        ► It must contain exactly 16 digits.
        ► It must only consist of digits (0-9).
        ► It may have digits in groups of 4, separated by one hyphen "-".
        ► It must NOT use any other separator like ' ' , '_', etc.
        ► It must NOT have 4 or more consecutive repeated digits.
        """
        pattern = '^(?:4\d{3}|5\d{3}|6\d{3})\-(?:\d{4})\-(?:\d{4})\-(?:\d{4})|^(?:4\d{15}|5\d{15}|6\d{15})'
        p = re.compile(pattern)

        if len(self.number) > 1:
            if p.match(self.number):
                self.number = self.number.replace('-', '')
                if len(self.number) <= 16:
                    return '{0}'.format(self.check_repeat(self.number))
                else:
                    return 'Invalid'
            else:
                return 'Invalid'

    @staticmethod
    def check_repeat(cc):
        """Check if there are consecutive digits more than 3 times."""
        control = 1
        last = ''
        for char in cc.replace('-', ''):
            if control < 4:
                if last == char:
                    control += 1
                else:
                    control = 1
            else:
                return 'Invalid'
            last = char
        return 'Valid'
