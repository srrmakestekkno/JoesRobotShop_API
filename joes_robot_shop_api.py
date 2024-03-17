from products import get_all_products
import UserCredentials
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
app.json.sort_keys = False
CORS(app)

cart = []

@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify(get_all_products())

@app.route("/api/cart", methods=["POST"])
def add_product():
   # Get the JSON data from the request body
    new_data = request.json
    
    # Ensure the request contains an array
    if not isinstance(new_data, list):
        return jsonify({'error': 'Data must be provided as an array'}), 400
    
    # Add each item in the array to the existing data list
    for item in new_data:
        cart.append(item)
    print(cart)
    # Return a success message
    return jsonify({'message': 'Data added successfully'}), 201
   

# @app.route("/api/cart", methods=["GET"])
# def get_cart():
#     return jsonify(cart)

# @app.route("/api/cart/<int:id>", methods=["DELETE"])
# def delete_item(id):
#     index = None
#     for i, item in cart:
#         if item["id"] == id:
#             index = i
#             break
        
#     if index is not None:
#         deleted_item = cart.pop(index)
#         return jsonify({"message": f"Item with id {id} deleted successfully",  'deleted_item': deleted_item}), 200
#     else :
#         return jsonify({"error": f"Data with id {id} not found"}), 404

@app.route("/api/sign-in", methods=["POST"])
def sign_in():
    input = request.json
    #print(f"Email is {input['email']}: password is {input['password']}")
    return jsonify({"message": "Success"}), 200

if __name__ == "__main__":
    app.run(debug =True)