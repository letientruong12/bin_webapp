import sqlite3

# Kết nối đến cơ sở dữ liệu (tạo mới nếu chưa tồn tại)
conn = sqlite3.connect("bin_database.db")
cursor = conn.cursor()

# Tạo bảng bin_data với các cột mới
cursor.execute("""
    CREATE TABLE IF NOT EXISTS bin_data (
        bin_number INTEGER,
        country TEXT,
        bank_name TEXT,
        card_name TEXT,
        card_type TEXT,
        provider_type TEXT,
        base TEXT,
        time_update TEXT,
        note TEXT
    )
""")

# Lưu thay đổi và đóng kết nối
conn.commit()
conn.close()
print("Đã tạo bảng thành công!")