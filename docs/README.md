# Project Documentation

This repository is a small Flask + SQLite application for searching BIN (Bank Identification Number) data via a web UI. It includes a minimal frontend (HTML + jQuery + Select2), a Flask backend, and utility scripts to create the database, import data, build indexes, and query data programmatically.

- App entrypoint: `app.py`
- Database file: `bin_database.db`
- HTML templates: `templates/`
- Static assets: `static/`
- Utility scripts: `create_database.py`, `import_data.py`, `create_indexes.py`, `check_data.py`, `query_data.py`

## Contents
- [Public API Reference](./api.md)
- [Python Modules and Scripts](./python-modules.md)
- [Frontend (Templates & JS)](./frontend.md)
- [Database Schema & Indexes](./database.md)
- [Usage & Examples](./usage.md)

## Quick Start
```bash
# 1) Create and activate a virtual environment (optional but recommended)
python3 -m venv .venv
source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Initialize database and import data
python create_database.py
# place bin_data.csv in project root, then:
python import_data.py
python create_indexes.py

# 4) Run the app
export PORT=5000  # optional, default 5000
python app.py
# Open http://localhost:5000
```
