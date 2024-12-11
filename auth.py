from flask import Blueprint, request, jsonify
import jwt  # Ensure you have the correct PyJWT package installed
import datetime

# Initialize the Blueprint for authentication
auth = Blueprint('auth', __name__)

# Secret key for encoding and decoding JWT
SECRET_KEY = "your_secret_key"

@auth.route('/login', methods=['POST'])
def login():
    # Parse the JSON data from the request
    data = request.json

    # Check username and password (this is a dummy validation for demonstration)
    if data['username'] == 'admin' and data['password'] == 'secretPass':
        # Generate a token with expiration time of 1 hour
        token = jwt.encode(
            {
                'user': data['username'], 
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }, 
            SECRET_KEY, 
            algorithm="HS256"
        )

        # Return the token as a JSON response
        return jsonify({'token': token}), 200

    # Return an error response for invalid credentials
    return jsonify({'message': 'Invalid credentials'}), 401
