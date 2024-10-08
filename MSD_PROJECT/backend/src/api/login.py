from flask import Blueprint, request, jsonify, session

auth_bp = Blueprint('auth_bp', __name__)

# 假设的用户数据库
users = {
    'patient': {'username': 'patient', 'password': 'password123', 'role': 'patient'},
    'doctor': {'username': 'doctor', 'password': 'password123', 'role': 'doctor'},
    'nurse': {'username': 'nurse', 'password': 'password123', 'role': 'nurse'}
}

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = users.get(username)

    if user and user['password'] == password:
        # 保存登录状态到 session
        session['user'] = user
        return jsonify({'message': f"Welcome {user['role']}!"}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()  # 清除session
    return jsonify({'message': 'Logged out successfully'}), 200
