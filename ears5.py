import sys
import aiohttp
import asyncio
import argparse

def append_to_output_file(message):
    version = 4 
    msg = "{} {}".format(version, message)
    with open("output.txt", "a") as output_file:
        output_file.write(msg)

async def fetch_dummy_data():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://34.145.40.53:8080/doDummy') as response:
            data = await response.text()  # Assuming the response is text, adjust if it's JSON or another format
            result = "Response from dummy endpoint: {}\n".format(data)
            append_to_output_file(result)
            return data

async def start_session():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://192.168.5.54:80/avend?action=start') as response:
            set_cookie_header = response.headers.getall('set-cookie')
            session_id = ';'.join(cookie.split(';')[0].split('=')[1] for cookie in set_cookie_header)
            result = "Session started\nSession ID: {}\n".format(session_id)
            append_to_output_file(result)
            return session_id
        
async def dispense_code(session_id, spool):
    headers = {
        'Cookie': f'sessionid={session_id}'
    }
    command = f"http://192.168.5.54:80/avend?action=dispense&code={spool}"
    result = "A {}\n".format(command)
    append_to_output_file(result)
    async with aiohttp.ClientSession(headers=headers) as session:
        append_to_output_file("B\n")
        async with session.get(command) as response:
            result = "Dispense code successful\n"
            append_to_output_file("C {}\n".format( result)) 

async def main2(args):
    result = "Loop indefinitely to listen to standard input!\n"
    append_to_output_file(result)
    
    line = args.input
    line = line.strip()
    pieces = line.split(",")
    if len(pieces) == 3:
        store, machine, spool = pieces
        session_id = await start_session()
        result = "store {} machine {} spool {} session_id {}\n".format(store, machine, spool, session_id)
        append_to_output_file(result)
        await dispense_code(session_id, spool)
    else:
        result = "Invalid input format: {}\nInput should be something like 1,1,34\n".format(line)
        append_to_output_file(result)

async def main():

    msg1 = "Loop indefinitely to listen to standard input!\n"
    append_to_output_file(msg1)

    for line in sys.stdin:
        line = line.strip()
        pieces = line.split(",")
        if len(pieces) == 3:
            store, machine, spool = pieces
            session_id = await start_session()
            msg2 = "store {} machine {} spool {} session_id {}\n".format( store, machine, spool, session_id)
            append_to_output_file(msg2)

            await dispense_code(session_id, spool)
            append_to_output_file("C ready again\n")
        else:
            append_to_output_file("Invalid input format: {}\n".format( line) )
            append_to_output_file("input should be something like 1,1,34\n")
if __name__ == "__main__":
    asyncio.run(main())



if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description='Process input from the command line.')
    # parser.add_argument('input', type=str, help='Input string in the format store,machine,spool')
    # args = parser.parse_args()
    asyncio.run(main(args))
