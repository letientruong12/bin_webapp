from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)

def get_unique_values(column):
    conn = sqlite3.connect("bin_database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT DISTINCT {column} FROM bin_data WHERE {column} IS NOT NULL ORDER BY {column}")
    values = [row[0] for row in cursor.fetchall()]
    conn.close()
    return values

@app.route("/get_options")
def get_options():
    countries = get_unique_values("country")
    bank_names = get_unique_values("bank_name")
    card_names = get_unique_values("card_name")
    card_types = get_unique_values("card_type")
    provider_types = get_unique_values("provider_type")
    return jsonify({
        "countries": countries,
        "bank_names": bank_names,
        "card_names": card_names,
        "card_types": card_types,
        "provider_types": provider_types
    })

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        bin_number = request.form.get("bin_number")
        country = request.form.get("country")
        bank_name = request.form.get("bank_name")
        card_name = request.form.get("card_name")
        card_type = request.form.get("card_type")
        provider_type = request.form.get("provider_type")
        time_update = request.form.get("time_update")
        note = request.form.get("note")

        conn = sqlite3.connect("bin_database.db")
        cursor = conn.cursor()

        query = "SELECT * FROM bin_data WHERE 1=1"
        params = []
        if bin_number:
            query += " AND bin_number = ?"
            params.append(bin_number)
        if country:
            query += " AND country = ?"
            params.append(country)
        if bank_name:
            query += " AND bank_name = ?"
            params.append(bank_name)
        if card_name:
            query += " AND card_name = ?"
            params.append(card_name)
        if card_type:
            query += " AND card_type = ?"
            params.append(card_type)
        if provider_type:
            query += " AND provider_type = ?"
            params.append(provider_type)
        if time_update:
            query += " AND time_update LIKE ?"
            params.append(f"%{time_update}%")
        if note:
            query += " AND note LIKE ?"
            params.append(f"%{note}%")

        query += " LIMIT 100"
        cursor.execute(query, params)
        results = cursor.fetchall()
        conn.close()

        return render_template("results.html", results=results)

    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Lấy port từ biến môi trường, mặc định 5000
    app.run(host="0.0.0.0", port=port, debug=False)  # Chạy trên tất cả interface, không dùng debug