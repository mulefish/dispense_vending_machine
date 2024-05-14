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
    # url = "http://localhost:8082/isOkToDispense"
    # headers = {
    #     'Content-Type': 'application/json',
    # }
    timestamp = datetime.now().isoformat()
    data = {
        "store": store,
        "machine": machine,
        "spool": spool,
        "timestamp": timestamp
    }
    # response = requests.post(url, headers=headers, json=data)
    # if response.status_code == 200:
    #     output = "Dispense code successful - " + response.text + "\n"
    # else:
    #     output = f"Failed to dispense code: {response.text}\n"
    store = data["store"]
    machine = data["machine"]
    spool = data["spool"]
    timestamp = data["timestamp"]
    output = "store {} machine {} spool {} timestamp {}".format(store, machine, spool, timestamp)
    with open('output.txt', 'a') as f:
        f.write(output)
        print(output)
    # return response.json()
    return data 

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
    count = 0 
    for line in sys.stdin:
        if len(line.strip()) > 0:
            count += 1  
            if count > 5: 
                print("exiting now {}".format(count))
                break  

            if "1,1,2" in line:
                print("Terminating loop due to signal 1,1,2")
                break
            else:
                print("Got this input |{}|".format( line ))
                session_id = start_session()
                print("session_id {}".format(session_id) ) 
            # print("LINE |{}|".format( line ))
            # candidate = parse_input(line)
            # if candidate["status"] == True:
            #     session_id = start_session()
            #     dispense_code(session_id);
            #     store = candidate["store"]
            #     machine = candidate["machine"]
            #     spool = candidate["spool"]
            #     result_as_json = isOkToDispense(store, machine, spool)
            #     print("result is: {}".format(result_as_json)) 
            # else:
            #     print("Rejected: " + line )
                