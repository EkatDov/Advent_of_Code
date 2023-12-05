
""" --- Day 1: Trebuchet?! 1.1 --- """

# open the input file and read the lines:
with open("day_1_input.txt", encoding="utf-8") as file:
    lines = file.readlines()


# set up a list to collect numbers from each line:
list_of_string_numbers = []
# iterate through the lines
for line in lines:
    number_in_line = ""
    # iterate through symbols of the line:
    for symbol in line:
        # collect all digit symbols in a string ...
        if symbol.isdigit():
            number_in_line += symbol
    # ... but only append the first and the last digit of that string. Double the single digit in a line
    list_of_string_numbers.append(number_in_line[0] + number_in_line[-1] if len(number_in_line) > 1 else number_in_line * 2)

# turn the string numbers into integers:
list_of_integers = [int(number) for number in list_of_string_numbers]
# sum the numbers up
result = sum(list_of_integers)

print(result)

