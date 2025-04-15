import sqlite3

def query_bin(bin_number=None, country=None, bank_name=None, card_type=None, 
              provider_type=None, time_update=None, note=None):
    conn = sqlite3.connect("bin_database.db")
    cursor = conn.cursor()

    # Xây dựng câu truy vấn
    query = "SELECT * FROM bin_data WHERE 1=1"
    params = []
    if bin_number:
        query += " AND bin_number = ?"
        params.append(bin_number)
    if country:
        query += " AND country LIKE ?"
        params.append(f"%{country}%")
    if bank_name:
        query += " AND bank_name LIKE ?"
        params.append(f"%{bank_name}%")
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

    # Thêm giới hạn để tránh tải nặng
    query += " LIMIT 100"

    # Thực thi truy vấn
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results

# Ví dụ sử dụng
results = query_bin(country="UNITED STATES",provider_type="PERSONAL")
for row in results[:5]:  # Hiển thị 5 dòng đầu
    print(row)