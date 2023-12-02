import re

def extract_coordinates(line):
    return re.sub(r"\D", "", line)

def word_to_digit(word):
    digit_map = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9
    }
    return mapping.get(word.lower(), "")

    
with open('calibration_doc.txt', 'r') as file:
    lines = file.readlines()

final_answer = 0
for i in lines:
    hidden_coordinates = (extract_coordinates(i))
    final_coordinate = hidden_coordinates[0] + hidden_coordinates[-1]
    final_answer += int(final_coordinate)
print(f"Final answer is: {final_answer}")