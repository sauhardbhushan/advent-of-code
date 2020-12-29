import pandas as pd
import string

def file_to_dict(lines):
    map = {}
    for i, line in enumerate(lines):
        map[i] = {}
        line = line.replace('\n', ' ')
        split_values = line.split(' ')
        for value in split_values:
            key = value.rpartition(':')[0]
            val = value.rpartition(':')[-1]
            map[i].update({ key: val })

    return map

with open('./day4.txt', 'r') as f1:
    lines = f1.read().split("\n\n")

map = file_to_dict(lines)
df = pd.DataFrame.from_dict(map).T.drop('cid', axis=1)


def is_between(value, lower, upper, valid_ndigits=4):
    try:
        ndigits = len(str(value))
        value = int(value)
    except ValueError:
        return False
    return lower <= value <= upper and ndigits == valid_ndigits


#  part 1
def count_valid_passports(df):
    nrows, _ = df.shape
    return nrows - df.isnull().any(axis=1).sum()


def validate(passport, key):
    if key == 'byr':
        return is_between(passport[key], 1920, 2002)
    if key == 'iyr':
        return is_between(passport[key], 2010, 2020)
    if key == 'eyr':
        return is_between(passport[key], 2020, 2030)
    if key == 'hgt':
        if type(passport[key]) != str:
            return False
        last_two_char = (passport[key])[-2:]
        if last_two_char == 'cm':
            return is_between(passport[key][:-2], 150, 193, 3)
        elif last_two_char == 'in':
            return is_between(passport[key][:-2], 59, 76, 2)
        return False
    if key == 'hcl':
        return all(char in set(string.hexdigits) for char in str(passport[key])[1:]) and str(passport[key])[0] == '#'
    if key == 'ecl':
        return passport[key] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    if key == 'pid':
        try:
            int(passport[key])
            return len(passport[key]) == 9
        except ValueError:
            return False


def is_passport_valid(passport):
    truth = []
    for key in passport.keys():
        truth.append(validate(passport, key))
    return all(truth)


df = df.T.to_dict()
# part 2
count = 0
for i, passport in df.items():
    print(i)
    if is_passport_valid(passport):
        count += 1

print(count)
