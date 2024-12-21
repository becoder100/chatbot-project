from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
import jwt
import datetime
from groq import Groq

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# MongoDB connection setup
client = MongoClient('mongodb://localhost:27017/')  # Update with your MongoDB connection string if necessary
db = client['chatapp']  # Use the chatapp database
users_collection = db['users']  # Collection to store user data
products_collection = db['products']
chats_collection = db['chats']

# Utility function to validate email and password
def validate_email(email):
    return "@" in email and "." in email

def validate_password(password):
    return len(password) >= 6

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirm_password')
    
    if not (name and email and password and confirm_password):
        return jsonify({'message': 'All fields are required'}), 400

    if users_collection.find_one({'email': email}):
        return jsonify({'message': 'Email is already registered'}), 400

    if password != confirm_password:
        return jsonify({'message': 'Passwords do not match'}), 400

    if not validate_email(email) or not validate_password(password):
        return jsonify({'message': 'Invalid email or password format'}), 400

    hashed_password = generate_password_hash(password)
    users_collection.insert_one({'name': name, 'email': email, 'password': hashed_password})
    return jsonify({'message': 'Signup successful'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not (email and password):
        return jsonify({'message': 'Email and password are required'}), 400

    user = users_collection.find_one({'email': email})
    if not user or not check_password_hash(user['password'], password):
        return jsonify({'message': 'Invalid email or password'}), 401

    token = jwt.encode({
        'email': email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({'message': 'Login successful', 'token': token}), 200

@app.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Token is missing'}), 401

    try:
        decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        email = decoded['email']
        user = users_collection.find_one({'email': email})
        if user:
            return jsonify({'message': f'Welcome {user["name"]}!', 'email': email}), 200
        else:
            return jsonify({'message': 'User not found'}), 404
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token'}), 401

client = Groq(api_key='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')

@app.route('/api/product', methods=['GET'])
def get_products():
    # Retrieve all documents from the 'products' collection
    products = products_collection.find()  # Use 'products_collection' here
    print(products)
    product_list = []
    
    # Loop through the documents and add them to a list
    for product in products:
        product['_id'] = str(product['_id'])  # Convert ObjectId to string
        product_list.append(product)
    
    return jsonify(product_list), 200

@app.route('/chat', methods=['POST'])
def chat():
    # Check for Authorization header
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"error": "Unauthorized: Missing or invalid Authorization header"}), 401

    # Extract the token
    token = auth_header.split(" ")[1]

    # Verify the token
    try:
        decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        user_email = decoded_token['email']
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Unauthorized: Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Unauthorized: Invalid token"}), 401

    # Retrieve messages from the request body
    messages = request.json.get("messages")

    if not messages:
        return jsonify({"error": "No messages provided"}), 400

    # Create a completion request using the Groq client
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=messages,
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )

        # Collect the response content and build the chat log
        response_content = ""
        for chunk in completion:
            response_content += chunk.choices[0].delta.content or ""

        # Append assistant's response to the messages
        messages.append({"role": "assistant", "content": response_content})

        # Store the chat log in the database
        chat_entry = {
            "email": user_email,
            "messages": messages
        }
        chats_collection.insert_one(chat_entry)

        # Return the assistant's response
        return jsonify({"response": response_content})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
