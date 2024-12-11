from flask import Blueprint, request, jsonify
import jwt 
import datetime

auth = Blueprint('auth', __name__)

SECRET_KEY = "your_secret_key"

@auth.route('/login', methods=['POST'])
def login():
    data = request.json

    if data['username'] == 'admin' and data['password'] == 'secretPass':
        token = jwt.encode(
            {
                'user': data['username'], 
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }, 
            SECRET_KEY, 
            algorithm="HS256"
        )

        return jsonify({'token': token}), 200

    return jsonify({'message': 'Invalid credentials'}), 401
