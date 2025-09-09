from modules.utils.remove_comments import sanitize
import os

def parse_contract(contract) -> list:
    sanitized_contract = sanitize(contract)
    tmp_file = open("./uncommented.txt", "w")
    tmp_file.write(sanitized_contract)
    tmp_file.close()
    with open("./uncommented.txt", 'r', encoding="utf-8") as f:
        lines = [line.rstrip('\n') for line in f]  # Remove newline characters
    os.remove("./uncommented.txt")
    return lines