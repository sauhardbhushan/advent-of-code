
with open('./day1.txt', 'r') as f1:
    lines = f1.readlines()
    numbers = [int(e.strip()) for e in lines]

sorted_nums = sorted(numbers)


def get_2_that_add_to(sorted_nums, target=2020):
    lower_pointer = 0
    upper_pointer = len(sorted_nums)-1
    num1 = None
    num2 = None

    while not (lower_pointer >= upper_pointer or upper_pointer <= lower_pointer):
        sum = sorted_nums[lower_pointer] + sorted_nums[upper_pointer]
        if sum < target:
            lower_pointer += 1
        elif sum > target:
            upper_pointer -= 1
        else:
            num1, num2 = sorted_nums[lower_pointer], sorted_nums[upper_pointer]
            break

    return num1, num2


for num in sorted_nums:
    num2, num3 = get_2_that_add_to(sorted_nums, target=2020-num)
    if type(num2) == int and type(num3) == int:
        print(num, num2, num3, num*num2*num3)
        break







