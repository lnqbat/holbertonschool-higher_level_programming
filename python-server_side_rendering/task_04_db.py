from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

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
    except Exception:
        raise
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
                products_list = json.load(f)
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
        elif source == "sql":
            try:
                products_list = read_products_from_sqlite()
            except Exception:
                error = "Error read DB SQLite."
                products_list = []
        else:
            error = "Wrong source"
            products_list = []
    except Exception:
        error = f"Error read files {source.upper()}."
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
