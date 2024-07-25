import sys
import aiohttp
from datetime import datetime
import asyncio

async def start_session():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://192.168.5.54:80/avend?action=start') as response:
            set_cookie_header = response.headers.getall('set-cookie')
            session_id = ';'.join(cookie.split(';')[0].split('=')[1] for cookie in set_cookie_header)
            result = "Session started\nSession ID: {}\n".format(session_id)
            with open("output.txt", "a") as output_file:
                output_file.write(result)
            return session_id
        
async def dispense_code(session_id, spool):
    headers = {
        'Cookie': f'sessionid={session_id}'
    }
    command = f"http://192.168.5.54:80/avend?action=dispense&code={spool}"
    result = f"{command}\n"
    with open("output.txt", "a") as output_file:
        output_file.write(result)
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(command) as response:
            result = "Dispense code successful\n"
            with open("output.txt", "a") as output_file:
                output_file.write(result)

async def main():
    version = 3
    result = "Version {} Loop indefinitely to listen to standard input!\n".format(version)
    with open("output.txt", "a") as output_file:
        output_file.write(result)
    
    for line in sys.stdin:
        line = line.strip()
        if line and len(line) > 3:
            pieces = line.split(",")
            if len(pieces) == 3:
                store, machine, spool = pieces
                session_id = await start_session()
                result = "A store {} machine {} spool {} session_id {}\n".format(store, machine, spool, session_id)
                with open("output.txt", "a") as output_file:
                    output_file.write(result)
                await dispense_code(session_id, spool)
                result = "B\n"
                with open("output.txt", "a") as output_file:
                    output_file.write(result)
            else:
                result = "Invalid input format |{}|\nInput should be something like 1,1,34\n".format(line)
                with open("output.txt", "a") as output_file:
                    output_file.write(result)
        else:
            result = "Skipping noise |{}|\n".format(line)
            with open("output.txt", "a") as output_file:
                output_file.write(result)

if __name__ == "__main__":
    asyncio.run(main())
