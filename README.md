# BIN Lookup Web App

A lightweight Flask application for searching a BIN (Bank Identification Number) dataset stored in SQLite. It provides an HTML UI for filtering, a small JSON endpoint for dropdown options, and simple Python helpers for scripted queries.

## Features
- HTML search form with filters (country, bank, card, provider, etc.)
- Server-side filtering against SQLite with a protective `LIMIT 100`
- JSON endpoint for populating dropdowns
- Operational scripts to create the database, import data, and create indexes

## Requirements
- Python 3.x
- `pip install -r requirements.txt`
  - Dependencies: `Flask`, `pandas`

## Quickstart
1. Create the database/table:
   ```bash
   python create_database.py
   ```
2. Import your data from CSV (expects `bin_data.csv` in the project root):
   ```bash
   # CSV should contain 9 columns in this order:
   # bin_number,country,bank_name,card_name,card_type,provider_type,base,time_update,note
   python import_data.py
   ```
3. Create helpful indexes:
   ```bash
   python create_indexes.py
   ```
4. Run the web app:
   ```bash
   export PORT=5000  # optional, defaults to 5000
   python app.py     # binds 0.0.0.0:$PORT
   ```
5. Open the UI at `http://localhost:5000/`.

## API & Developer Docs
- HTTP endpoints: see [`docs/HTTP_API.md`](docs/HTTP_API.md)
- Python APIs and scripts: see [`docs/Python_APIs.md`](docs/Python_APIs.md)
- Frontend templates, JS, and CSS: see [`docs/Frontend.md`](docs/Frontend.md)

## Example usage
- Fetch dropdown options (JSON):
  ```bash
  curl -s http://localhost:5000/get_options | jq
  ```
- Search via POST (HTML result):
  ```bash
  curl -X POST \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "country=UNITED STATES&card_type=CREDIT" \
    http://localhost:5000/
  ```
- Scripted query from Python:
  ```python
  from query_data import query_bin

  rows = query_bin(country="UNITED STATES", provider_type="PERSONAL")
  for row in rows:
      print(row)
  ```

## Notes
- The database file is `bin_database.db` in the project root.
- The import step replaces table contents (`if_exists="replace"`). Back up before importing if needed.
