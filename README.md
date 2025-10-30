# BIN Search App (Flask + SQLite)

A small web app to search BIN (Bank Identification Number) data with a Bootstrap frontend, Flask backend, and SQLite storage. Includes scripts to create the database, import CSV data, build indexes, and query data programmatically.

- App entry: `app.py`
- DB file: `bin_database.db`
- Docs: see [`docs/README.md`](./docs/README.md)

## Quick Start
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python create_database.py
# place bin_data.csv in project root
python import_data.py
python create_indexes.py
export PORT=5000
python app.py
# Open http://localhost:5000
```
