import pandas as pd
import sqlite3

# Đọc file CSV
df = pd.read_csv("bin_data.csv")

# Đổi tên cột để khớp với bảng SQLite (nếu cần)
df.columns = ["bin_number", "country", "bank_name", "card_name", "card_type", 
              "provider_type", "base", "time_update", "note"]

# Kết nối đến SQLite
conn = sqlite3.connect("bin_database.db")

# Nhập dữ liệu vào bảng bin_data
df.to_sql("bin_data", conn, if_exists="replace", index=False)

# Đóng kết nối
conn.close()
print("Đã nhập dữ liệu thành công!")