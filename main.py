from flask import Flask, request, jsonify,render_template
import carinfo
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/get-info', methods=['GET'])
def get_info():
    vin = request.args.get('vin')

    if vin is None:
        return jsonify({'error': 'VIN not provided'}), 400
    
    CarData=carinfo.getInfoByVin(vin)

    if 'exception'in CarData:
        return jsonify({'error': CarData['message']}), CarData['code']
        
    CarPhotos=carinfo.GetPhotos(CarData['make'] + " " +CarData['model'])
    response_data={
        'cardata': CarData,
        'photos' :CarPhotos
        
    }

    return jsonify(response_data)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
