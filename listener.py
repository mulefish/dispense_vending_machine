import sys
import requests
import json
from datetime import datetime
import re

def start_session():
    response = requests.get('http://192.168.5.54:80/avend?action=start')
    set_cookie_header = response.headers['set-cookie']
    session_id = set_cookie_header.split(';')[0].split('=')[1]

    print("Session started")
    print("Session ID:", session_id)

    return session_id

def dispense_code(session_id):
    headers = {
        'Cookie': f'sessionid={session_id}'
    }

    response = requests.get('http://192.168.5.54:80/avend?action=dispense&code=14', headers=headers)
    print("Dispense code successful")

def isOkToDispense(store, machine, spool):
    url = "http://localhost:8082/isOkToDispense"
    headers = {
        'Content-Type': 'application/json',
    }
    timestamp = datetime.now().isoformat()
    data = {
        "store": store,
        "machine": machine,
        "spool": spool,
        "timestamp": timestamp
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        output = "Dispense code successful - " + response.text + "\n"
    else:
        output = f"Failed to dispense code: {response.text}\n"
    with open('output.txt', 'a') as f:
        f.write(output)
        print(output)
    return response.json()

def parse_input(input_str):
    pattern = r'^(\d+),(\d+),(\d+)$'
    match = re.match(pattern, input_str)
    if match:
        store, machine, spool = map(int, match.groups())
        return {"status":True,"store": store, "machine": machine, "spool": spool}
    else:
        return {"status":False}



if __name__ == "__main__":
    print("Loop indefinitely to listen to standard input")
    for line in sys.stdin:
        if len(line.strip()) > 0:

            candidate = parse_input(line)
            if candidate["status"] == True:
                #session_id = start_session()
                store = candidate["store"]
                machine = candidate["machine"]
                spool = candidate["spool"]
                result_as_json = isOkToDispense(store, machine, spool)
                print(result_as_json)
            else:
                print("Rejected: " + line )
                