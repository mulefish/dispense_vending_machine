import re

def parse_input(input_str):
    pattern = r'^(\d+),(\d+),(\d+)$'
    match = re.match(pattern, input_str)
    if match:
        store, machine, spool = map(int, match.groups())
        return {"status":True,"store": store, "machine": machine, "spool": spool}
    else:
        return {"status":False}

# Test the function
input_str = "4,2,622"
result = parse_input(input_str)
print(result)  # Output: {'store': 4, 'machine': 2, 'spool': 6}

input_str = "2,4,6,8"
result = parse_input(input_str)
print(result)  # Output: NOPE
