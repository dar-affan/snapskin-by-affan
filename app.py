from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)


# ---------- HOME PAGE ----------
@app.route("/")
def home():
    try:
        with open("products.json", "r", encoding="utf-8") as f:
            products = json.load(f)
    except:
        products = []

    return render_template("index.html", products=products)


# ---------- ADMIN PAGE (OPTIONAL) ----------
@app.route("/admin")
def admin():
    return render_template("admin.html")


# ---------- API : PRODUCTS ----------
@app.route("/api/products")
def api_products():
    try:
        with open("products.json", "r", encoding="utf-8") as f:
            products = json.load(f)
    except:
        products = []

    return jsonify(products)


# ❌ DO NOT ADD app.run()
# Render / Hosting khud start karta hai
