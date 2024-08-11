from flask import Flask, render_template, send_file, request, jsonify
import qrcode

app = Flask(__name__)


@app.route('/qrcode', methods=['GET', 'POST'])
def generate_qrcode():

    # create qr code instance
    qr = qrcode.QRCode(version=1, box_size=10, border=5)

    itemToReach = {}
    itemToReach['storeId_fk']=1
    itemToReach['machineId']="WarmMoon"
    itemToReach['spoolId']="A1"

    qr.add_data(itemToReach)
    qr.make(fit=True)
    
    # generate qr code image
    img = qr.make_image(fill_color='black', back_color='white')

    # # save qr code image to a buffer
    # buffer = io.BytesIO()
    # img.save(buffer, format='PNG')
    # buffer.seek(0)

    # # send qr code image as a file
    # return send_file(buffer, mimetype='image/png')
    # save qr code image to a temporary file
    img_file = 'temp_qrcode.png'
    img.save(img_file)
    
    # send qr code image as a file
    return send_file(img_file, mimetype='image/png')

@app.route('/isOkToDispense', methods=['POST'])
def isOkToDispense():
    # Check if the request contains JSON data
    if request.is_json:
        # Get the JSON data from the request
        json_data = request.get_json()
        # Return the received JSON data
        return jsonify(json_data), 200
    else:
        # If the request does not contain JSON data, return an error
        return jsonify({"error": "Request must contain JSON data"}), 400

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/qr')
def qr():
    return render_template('qr.html')


if __name__ == '__main__':
    app.run(debug=True, port=8082)
    print("SEE http://localhost:8082/ ")
    print("or better yet see ")
    print("http://localhost:8082/qr")