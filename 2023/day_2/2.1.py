import re

""" Day 2: Cube Conundrum """

# read the input as a list of lines
with open("day_2_input.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# define the max number of balls in the sack
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

# prepare the regex patterns
game_pattern = r"Game ([1-9][0-9]?0?)"
red_pattern = r"(\d*) red"
green_pattern = r"(\d*) green"
blue_pattern = r"(\d*) blue"


def compare_numbers(list_of_numbers: list, max_number: int) -> bool:
    """ return False if any number in the list is greater than the max number;
    return True if none of the numbers in the list is greater than the max number """
    for number in list_of_numbers:
        if number > max_number:
            return False
    return True


def turn_str_into_int(list_of_str: list) -> list:
    """ converse the list of strings into a list of integers """
    return [int(number) for number in list_of_str]

# save the current sum of game IDs
sum_game_ids = 0

for line in lines:
    # get a list of all numbers of red balls
    all_red_strings = re.findall(red_pattern, line)
    all_red_ints = turn_str_into_int(all_red_strings)

    # get a list of all numbers of green balls
    all_green_strings = re.findall(green_pattern, line)
    all_green_ints = turn_str_into_int(all_green_strings)

    # get a list of all numbers of blue balls
    all_blue_strings = re.findall(blue_pattern, line)
    all_blue_ints = turn_str_into_int(all_blue_strings)

    # check_<colour> is True if none of the ball numbers is greater as the respective colour's max number
    check_reds = compare_numbers(all_red_ints, MAX_RED)
    check_greens = compare_numbers(all_green_ints, MAX_GREEN)
    check_blues = compare_numbers(all_blue_ints, MAX_BLUE)

    # only get the game IDs if all three check_<colour> evaluate to True
    if check_reds and check_greens and check_blues:
        match_game_id = re.match(game_pattern, line)
        valid_game_id = int(match_game_id.group(1))
        sum_game_ids += valid_game_id

print(sum_game_ids)