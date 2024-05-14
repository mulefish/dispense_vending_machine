import sys
import aiohttp
import json
from datetime import datetime
import re
import asyncio


async def start_session():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://192.168.5.54:80/avend?action=start') as response:
            set_cookie_header = response.headers.getall('set-cookie')
            session_id = ';'.join(cookie.split(';')[0].split('=')[1] for cookie in set_cookie_header)
            print("Session started")
            print("Session ID:", session_id)
            return session_id
        
async def dispense_code(session_id):
    headers = {
        'Cookie': f'sessionid={session_id}'
    }
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get('http://192.168.5.54:80/avend?action=dispense&code=14') as response:
            print("Dispense code successful")


async def main():
    DEBUG=False
    count = 0 
    last_line = "" 
    if DEBUG == True:
        session_id = await start_session()
        await dispense_code(session_id)

    print("Loop indefinitely to listen to standard input")
    count = 0 
    for line in sys.stdin:

if len(line.strip()) > 0:

            if "1,1,24" in line:
                print("{} Terminating loop due to signal 1,1,2".format(count))
                break
            else:
                if line != last_line:
                    last_line = line
                    print("{} Got this input |{}|".format( count, line ))
                    session_id = await start_session()
                    await dispense_code(session_id)
                else: 
                    print("Skipping {} {} ".format( line , last_line))

if __name__ == "__main__":
    asyncio.run(main())