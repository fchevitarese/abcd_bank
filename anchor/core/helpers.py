import re


def read_file(file):
    """Receive the file with the card numbers.
    Constraints: 0 < N < 100
    The first line of input contains an integer N.
    The next N lines contain credit card numbers.
    """
    with open(file, 'r') as cards:
        data = cards.readlines()
        if int(data[0] > 0 and int(data[0]) <= 100):
            for cc in data[1:]:
                if len(cc) == 1:
                    pass
                print(check_valid(cc))


def check_valid(ccnumber):
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

    if p.match(ccnumber):
        ccnumber = ccnumber.replace('-', '')
        if len(ccnumber) <= 16:
            return '{0}'.format(check_repeat(ccnumber))
        else:
            return 'Invalid'
    else:
        return 'Invalid'


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

