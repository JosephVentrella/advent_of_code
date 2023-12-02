import re

def extract_numbers(line):
    return re.sub(r"\D", "", line)
    
with open('calibration_doc.txt', 'r') as file:
    lines = file.readlines()

final_answer = 0
for i in lines:
    val = (extract_numbers(i))
    # print(val)
    final_coordinate = val[0] + val[-1]
    final_coordinate = int(final_coordinate)
    print(final_coordinate)
    final_answer += final_coordinate
print(f"Final answer is: {final_answer}")