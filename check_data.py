import sqlite3

conn = sqlite3.connect("bin_database.db")
cursor = conn.cursor()

# Đếm số dòng
cursor.execute("SELECT COUNT(*) FROM bin_data")
total_rows = cursor.fetchone()[0]
print(f"Tổng số dòng: {total_rows}")

# Xem 5 dòng đầu
cursor.execute("SELECT * FROM bin_data LIMIT 5")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()