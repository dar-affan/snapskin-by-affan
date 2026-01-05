from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PRODUCT_FILE = os.path.join(BASE_DIR, "products.json")


def load_products():
    if not os.path.exists(PRODUCT_FILE):
        return []
    with open(PRODUCT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_products(data):
    with open(PRODUCT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


@app.route("/")
def home():
    products = load_products()
    return render_template("index.html", products=products)


@app.route("/admin", methods=["GET", "POST"])
def admin():
    products = load_products()

    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        image = request.form["image"]

        products.append({
            "name": name,
            "price": price,
            "image": image
        })

        save_products(products)
        return redirect(url_for("admin"))

    return render_template("admin.html", products=products)


@app.route("/delete/<int:index>")
def delete(index):
    products = load_products()
    if index < len(products):
        products.pop(index)
        save_products(products)
    return redirect(url_for("admin"))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)