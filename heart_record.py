from flask import Flask, jsonify, request

app = Flask(__name__)

heart_record = [
    {
        "heart_id": "123",
        "date": "10/10/10",
        "heart_rate": "120 BPM"
    },
    {
        "heart_id": "321",
        "date": "11/11/11",
        "heart_rate": "94 BPM"
    }
]


@app.route('/heartnum/<heart_id1>', methods=['GET']) 
def getHeart(heart_id1):     
    heart_data = None     
    for info in heart_record:         
        if info['heart_id'] == heart_id1:             
            heart_data = info      
            if heart_data:         
                return jsonify(heart_data)     
            else:         
                return jsonify({"error": "Heart information not found"}), 404


@app.route('/heart_record', methods=['POST'])
def addHeart():
    new_heart_record= request.get_json()
    if new_heart_record:
        heart_record.append(heart_record)
        return jsonify({"Successful": True, "heart_record_added": new_heart_record}), 201
    else:
        return jsonify({"error": "No data provided"}), 400

@app.route('/heart_record/<int:index>', methods=['DELETE'])
def delHeart(index):
    if 0 <= index < len(heart_record):
        deleted_heart_record = heart_record.pop(index)
        return jsonify({"Successful": True, "heart_record_deleted": deleted_heart_record}), 200
    else:
        return jsonify({"error": "Index out of range"}), 400

@app.route('/heartnum/<heart_id>', methods=['PUT']) 
def update_heart_info(heart_id):     
    heart_data = None     
    for info in heart_record :         
        if info['heart_id'] == heart_id:             
            heart_data = info     
            if heart_data:         
                data = request.get_json()         
                heart_data['date'] = data.get('date', heart_data['date'])         
                heart_data['heart_rate'] = data.get('heart_rate', heart_data['heart_rate'])         
                return jsonify({"message": "Heart record updated successfully", "updated_record": heart_data}), 200     
            else:         
                return jsonify({"error": "Heart information not found"}), 404


if __name__ == '__main__':
    app.run()