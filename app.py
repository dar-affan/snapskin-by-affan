from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dummy products (backend se aa rahe hain)
PRODUCTS = {
    "physical": [
        {"id": 1, "name": "Anime Phone Skin", "price": 299},
        {"id": 2, "name": "Marble Phone Skin", "price": 249},
        {"id": 3, "name": "Custom Name Skin", "price": 349},
    ],
    "digital": [
        {"id": 101, "name": "Wallpaper Pack", "price": 99},
        {"id": 102, "name": "Aesthetic Icons", "price": 149},
    ]
}

@app.route("/")
def home():
    return render_template("index.html", products=PRODUCTS)

@app.route("/order", methods=["POST"])
def order():
    name = request.form.get("name")
    phone = request.form.get("phone")
    product = request.form.get("product")

    print("📦 NEW ORDER RECEIVED")
    print("Name:", name)
    print("Phone:", phone)
    print("Product:", product)

    return jsonify({"status": "success", "message": "Order received"})

if __name__ == "__main__":
    app.run(debug=True)
