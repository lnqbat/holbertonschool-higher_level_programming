from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json') as f:
        data = json.load(f)
    items_list = data.get("items", [])
    return render_template('items.html', items=items_list)

def read_products_from_sqlite():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                "id": int(row[0]),
                "name": row[1],
                "category": row[2],
                "price": float(row[3])
            })
    finally:
        if 'conn' in locals():
            conn.close()
    return products

@app.route('/products')
def products():
    source = request.args.get("source", "json")
    prod_id = request.args.get("id")
    products_list = []
    error = None

    try:
        if source == "json":
            with open('products.json', encoding='utf-8') as f:
                data = json.load(f)
            products_list = data
        elif source == "csv":
            with open('products.csv', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                products_list = [
                    {
                        "id": int(row["id"]),
                        "name": row["name"],
                        "category": row["category"],
                        "price": float(row["price"])
                    }
                    for row in reader
                ]
        else:
            error = "Wrong source"
            products_list = []
    except Exception:
        error = f"Erreur lors de la lecture du fichier {source.upper()}."
        products_list = []

    if prod_id and not error:
        try:
            pid = int(prod_id)
            filtered = [p for p in products_list if int(p["id"]) == pid]
            if filtered:
                products_list = filtered
            else:
                error = "Product not found"
                products_list = []
        except Exception:
            error = "Invalid id value"
            products_list = []

    return render_template('product_display.html', products=products_list, error=error)

if __name__ == '__main__':
    app.run(debug=True)
