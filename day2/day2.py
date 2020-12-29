
with open('./day2.txt', 'r') as f1:
    lines = f1.read().splitlines()
    policies = [line.split(': ')[0] for line in lines]
    passwords = [line.split(': ')[1] for line in lines]


def parse_policy(policy):
    count, char = policy.split(' ')
    min, max = count.split('-')

    return int(min), int(max), char


def char_count(string, char):
    counter = 0
    for character in string:
        if char == character:
            counter += 1

    return counter


# part 1
parsed_policies = [parse_policy(policy) for policy in policies]
valid_count = 0
for i, pwd in enumerate(passwords):
    min, max, char = parsed_policies[i]
    n_chars = char_count(pwd, char)

    if int(min) <= n_chars <= int(max):
        valid_count += 1

print(valid_count)


# part 2
valid_count = 0
for i, pwd in enumerate(passwords):
    lower_index, upper_index, character = parsed_policies[i]
    if pwd[lower_index - 1] == character or pwd[upper_index - 1] == character and pwd[lower_index - 1] != pwd[upper_index - 1]:
        valid_count += 1

print(valid_count)




