import re

number_eq = {
    "one": "1", "two": "2", "three": "3",
    "four": "4", "five": "5", "six": "6",
    "seven": "7", "eight": "8", "nine": "9"
}

def solve(input_list):
    exp = re.compile("(?=("+"|".join(number_eq.keys())+"|"+"|".join(number_eq.values())+"))")
    numbers = []
    for element in input_list:
        all_matches = exp.findall(element)
        match1 = number_eq[all_matches[0]] if all_matches[0] in number_eq.keys() else all_matches[0]
        match2 = number_eq[all_matches[-1]] if all_matches[-1] in number_eq.keys() else all_matches[-1]
        number = int(match1 + match2)
        numbers.append(number)

    return sum(numbers)