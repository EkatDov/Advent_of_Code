from two_one import lines
from two_one import red_pattern, green_pattern, blue_pattern
from two_one import get_a_list_of_numbers

sum_of_powers = 0

for line in lines:
    # get the max number of each colour balls in each game:
    max_red = max(get_a_list_of_numbers(line, red_pattern))
    max_green = max(get_a_list_of_numbers(line, green_pattern))
    max_blue = max(get_a_list_of_numbers(line, blue_pattern))
    # calculate the powers by multiplying the max red, green and blue number
    power = max_red * max_green * max_blue
    # add the power of each game to the common sum
    sum_of_powers += power

if __name__ == "__main__":
    print(sum_of_powers)