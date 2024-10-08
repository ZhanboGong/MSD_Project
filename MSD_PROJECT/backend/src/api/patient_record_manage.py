from flask import Flask, request, jsonify

app = Flask(__name__)

# 模拟数据库
patient_records = []

# 增加医疗记录
@app.route('/records', methods=['POST'])
def add_record():
    data = request.get_json()
    patient_records.append(data)
    return jsonify({"message": "Record added successfully", "record": data}), 201

# 修改医疗记录
@app.route('/records/<int:record_id>', methods=['PUT'])
def update_record(record_id):
    data = request.get_json()
    if 0 <= record_id < len(patient_records):
        patient_records[record_id] = data
        return jsonify({"message": "Record updated successfully", "record": data}), 200
    return jsonify({"message": "Record not found"}), 404

# 删除医疗记录
@app.route('/records/<int:record_id>', methods=['DELETE'])
def delete_record(record_id):
    if 0 <= record_id < len(patient_records):
        deleted_record = patient_records.pop(record_id)
        return jsonify({"message": "Record deleted successfully", "record": deleted_record}), 200
    return jsonify({"message": "Record not found"}), 404
