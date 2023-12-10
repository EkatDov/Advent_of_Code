""" --- Day 1: Trebuchet?! 1.2 --- """

def get_first_number(line, numbers_list):
    """
    This function finds and returns the first number of the string as a digit.
    If the number is spelled out in letters, the function substitutes it with the corresponding digit.
    :param line -> string
    :param numbers_list -> list of numbers (mixed digits and letters)
    """
    # set up the variables to keep track of the number that is closest to the beginning of the line:
    current_index = len(line)
    current_number = ""
    # iterate over the list of numbers to find matches in the line:
    for number in numbers_list:
        # var i stores the index of the number (or starting symbol of it) that is found in this iteration
        i = line.find(number)
        # if the number at index i is closer to the beginning (exclude index -1 which stands for unmatched numbers) ...
        if i <= current_index and i != -1:
            # save the index and the number itself as current number:
            current_index = i
            # the last number to be the current number is the number we are looking for (closest to the beginning of the string)
            current_number = number
    # if we got a spelled out number, override it with the list item that follows it (which is its digital equivalent)
    if current_number.isalpha():
        current_number = numbers_list[numbers_list.index(current_number) + 1]

    return current_number

# open the input file and read the lines:
with open("day_1_input.txt", encoding="utf-8") as file:
    lines = file.readlines()

# set up the list to record all 2-digit numbers from each line
list_of_values = []
# set up the list of numbers
numbers = ["one", "1", "two", "2", "three", "3", "four", "4", "five", "5", "six", "6", "seven", "7", "eight", "8", "nine", "9"]
# set up the list of inverted numbers
inverted_numbers = [number[::-1] for number in numbers]

# iterate over each line:
for line in lines:
    # invert the line to get the last digit
    inverted_line = line[::-1]
    first_number = get_first_number(line, numbers)
    last_number = get_first_number(inverted_line, inverted_numbers)
    list_of_values.append(first_number + last_number)

# turn the string numbers into integers:
list_of_integers = [int(number) for number in list_of_values]
# sum the numbers up
result = sum(list_of_integers)
print(result)
