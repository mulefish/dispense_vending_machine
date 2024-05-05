from flask import Flask, render_template, send_file
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


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8082)
