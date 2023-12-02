import re

def extract_coordinates(line):
    return re.sub(r"\D", "", line)
    
with open('calibration_doc.txt', 'r') as file:
    lines = file.readlines()

final_answer = 0
for i in lines:
    hidden_coordinates = (extract_coordinates(i))
    final_coordinate = hidden_coordinates[0] + hidden_coordinates[-1]
    final_answer += int(final_coordinate)
print(f"Final answer is: {final_answer}")