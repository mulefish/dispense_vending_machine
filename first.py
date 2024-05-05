import sys
import requests

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

    # response = requests.get('http://192.168.5.54:80/avend?action=dispense&code=14', headers=headers)
    print("Dispense code successful")

if __name__ == "__main__":
    print("Loop indefinitely to listen to standard input")
    for line in sys.stdin:
        session_id = start_session()
        if len(line.strip()) >0:
                # Dispense code
                dispense_code(session_id)
