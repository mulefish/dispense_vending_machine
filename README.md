# dispense_vending_machine
Code for the dispense vending machine

# QR Code test page usage
python test_server.py        
http://localhost:8082/  
Click a button to see a QR  

# DONE: 
1: Read actual input from the QR codes
2: Test harness ( Restful end point ) 
3: Serve a webpage that show the recent history of the vending machine and its current state ( password protected ) 
4: Call GCP's DB to verify that it is OK to dispense a given spool 

# TODO:
Actually call the API. Currently spoofing that by running 'python test_server.py' ( http://localhost:8082/ )  
and also 'python listener.py' 

# QRCode:
There are many ways to make a QR code. Currently using one from https://davidshimjs.github.io/qrcodejs/  
See qrcode.min.js in the /static dir   
TODO: STOP using this library ( because it is a MIT license, which is OK but I can roll my own such that zero license issues need be thought about )