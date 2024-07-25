import sys
import aiohttp
import asyncio

async def fetch_dummy_data():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://34.145.40.53:8080/doDummy') as response:
            data = await response.text()  # Assuming the response is text, adjust if it's JSON or another format
            print("Response from dummy endpoint:", data)
            return data

async def start_session():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://192.168.5.54:80/avend?action=start') as response:
            set_cookie_header = response.headers.getall('set-cookie')
            session_id = ';'.join(cookie.split(';')[0].split('=')[1] for cookie in set_cookie_header)
            print("Session started")
            print("Session ID:", session_id)
            return session_id

async def dispense_code(session_id, spool):
    headers = {
        'Cookie': f'sessionid={session_id}'
    }
    command = f"http://192.168.5.54:80/avend?action=dispense&code={spool}"
    print(command)
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(command) as response:
            print("Dispense code successful")

async def main():
    print("!! Loop indefinitely to listen to standard input!")
    loop_count = 0
    for line in sys.stdin:
        loop_count += 1 
        print(line)
        if loop_count > 3:
            print("exiting now")
            break 

    # await fetch_dummy_data()
    # session_id = await start_session()
    # await dispense_code(session_id, 12)

    #print("exit now")

    # for line in sys.stdin:
    #     loop_count += 1
    #     if loop_count > 3:
    #         print("Processed 3 inputs, exiting.")
    #         break
        
    #     line = line.strip()
    #     # print("store {} machine {} spool {}".format(store, machine, spool))
    #     await fetch_dummy_data()
    #     session_id = await start_session()
    #     await dispense_code(session_id, 12)

        # pieces = line.split(",")
        # if len(pieces) == 3:
        #     store, machine, spool = pieces
        #     print("store {} machine {} spool {}".format(store, machine, spool))
        #     await fetch_dummy_data()
        #     session_id = await start_session()
        #     await dispense_code(session_id, spool)
        # else:
        #     print("Invalid input format:", line)

if __name__ == "__main__":
    asyncio.run(main())
