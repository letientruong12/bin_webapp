# HTTP API Reference

This document describes the public HTTP endpoints exposed by the Flask application in `app.py`.

## Base URL
- Default (local): `http://localhost:5000`
- You can change the port via the `PORT` environment variable when starting the app.

## Authentication
- None. All endpoints are public.

---

## GET /get_options
Returns distinct values for dropdowns used by the UI. Values are derived from the `bin_data` table in `bin_database.db`.

- **Method**: `GET`
- **URL**: `/get_options`
- **Query params**: None
- **Response: 200 OK (application/json)**
  ```json
  {
    "countries": ["UNITED STATES", "VIETNAM", "..."],
    "bank_names": ["BANK A", "BANK B", "..."],
    "card_names": ["VISA", "MASTERCARD", "..."],
    "card_types": ["CREDIT", "DEBIT", "..."],
    "provider_types": ["PERSONAL", "BUSINESS", "..."]
  }
  ```
- **Notes**:
  - Lists may be empty if the database has no data.
  - The values are sorted ascending and exclude `NULL`.

- **Example**
  ```bash
  curl -s http://localhost:5000/get_options | jq
  ```

---

## GET /
Renders the search form (HTML).

- **Method**: `GET`
- **URL**: `/`
- **Response: 200 OK (text/html)**
  - Returns the search page defined in `templates/index.html`.

- **Example**
  - Open in a browser: `http://localhost:5000/`

---

## POST /
Executes a search against `bin_data` and renders results (HTML). The server applies a `LIMIT 100` to protect performance.

- **Method**: `POST`
- **URL**: `/`
- **Content-Type**: `application/x-www-form-urlencoded`
- **Form fields (all optional unless stated)**:
  - `bin_number` (exact match)
  - `country` (exact match)
  - `bank_name` (exact match)
  - `card_name` (exact match)
  - `card_type` (exact match)
  - `provider_type` (exact match)
  - `time_update` (substring match; e.g., `YYYY-MM-DD`)
  - `note` (substring match)

- **Response: 200 OK (text/html)**
  - Renders `templates/results.html` with at most 100 rows.

- **Examples**
  - Search by country and card type:
    ```bash
    curl -X POST \
      -H "Content-Type: application/x-www-form-urlencoded" \
      -d "country=UNITED STATES&card_type=CREDIT" \
      http://localhost:5000/
    ```
  - Search by `bin_number` only:
    ```bash
    curl -X POST \
      -H "Content-Type: application/x-www-form-urlencoded" \
      -d "bin_number=457173" \
      http://localhost:5000/
    ```

- **Notes**
  - Returns HTML, not JSON.
  - Exact-match fields compare using equality; `time_update` and `note` use `LIKE '%value%'`.
  - Database file: `bin_database.db` (SQLite). Ensure it exists and is populated.

---

## Server startup
```bash
# Install deps
pip install -r requirements.txt

# (Optional) set the port
export PORT=5000

# Run the server
python app.py  # binds 0.0.0.0:$PORT (default 5000)
```
