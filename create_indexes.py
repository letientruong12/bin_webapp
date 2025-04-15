import sqlite3

conn = sqlite3.connect("bin_database.db")
cursor = conn.cursor()

# Tạo index cho các cột thường truy vấn
cursor.execute("CREATE INDEX IF NOT EXISTS idx_bin_number ON bin_data(bin_number)")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_country ON bin_data(country)")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_bank_name ON bin_data(bank_name)")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_card_type ON bin_data(card_type)")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_provider_type ON bin_data(provider_type)")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_time_update ON bin_data(time_update)")


conn.commit()
conn.close()
print("Đã tạo index thành công!")