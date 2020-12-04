from functools import reduce
from itertools import combinations
from collections import defaultdict
import re


def valid_range(min_num, max_num):
    def wrapped(data):
        try:
            return min_num <= int(data) <= max_num
        except:
            return False
    return wrapped

def valid_regex(regex):
    def wrapped(data):
        try:
            return re.match(regex, data)
        except:
            return False
    return wrapped

def valid_height(data):
    try:
        if data.endswith("cm"):
            return valid_range(150, 193)(data.replace("cm", ""))
        if data.endswith("in"):
            return valid_range(59, 76)(data.replace("in", ""))
        return False
    except:
        return False

all_attrs = {
        "byr": valid_range(1920, 2002),
        "iyr": valid_range(2010, 2020),
        "eyr": valid_range(2020, 2030),
        "hgt": valid_height,
        "hcl": valid_regex(r"^#[0-9a-f]{6}$"),
        "ecl": valid_regex(r"^amb|blu|brn|gry|grn|hzl|oth$"),
        "pid": valid_regex(r"^[0-9]{9}$"),
}

class Passport(object):
    def __init__(self, line):
        self.line = line
        self.attrs = dict([
            tuple(token.split(":"))
            for token in line.split()
        ])

    def all_present(self):
        data = {
            attr: attr in self.attrs.keys()
            for attr in all_attrs.keys()
        }
        return all(data.values())

    def is_valid(self):
        for (attr, validation) in all_attrs.items():
            if not attr in self.attrs.keys():
                return False

            valid = validation(self.attrs[attr])
            if not valid:
                return False
        return True

passports = []
with open('input', 'r') as f:
    all_data = f.read()
    passports = [
        Passport(line.strip())
        for line in all_data.split("\n\n")
    ]
print("one")
print(sum([
    1
    for passport in passports
    if passport.all_present()
]))

print("two")
print(sum([
    1
    for passport in passports
    if passport.is_valid()
]))
