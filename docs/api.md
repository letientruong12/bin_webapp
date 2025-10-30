# Public API Reference

The application exposes a small set of HTTP endpoints using Flask.

## GET `/get_options`
Returns lists of distinct values for dropdowns used by the UI.

- Method: `GET`
- Response: `application/json`
- Auth: None

Example:
```bash
curl -s http://localhost:5000/get_options | jq
```

Response schema:
```json
{
  "countries": ["..."],
  "bank_names": ["..."],
  "card_names": ["..."],
  "card_types": ["..."],
  "provider_types": ["..."]
}
```

Notes:
- Values are fetched from the `bin_data` table where the corresponding column is not NULL.
- Results are ordered.

## `GET|POST` `/`
Renders the search page (GET) or processes a search (POST) and returns an HTML results page.

- Methods: `GET`, `POST`
- Response: `text/html`
- Auth: None

### GET `/`
Returns the search form page.

Example:
```bash
curl -s http://localhost:5000/ | head -n 20
```

### POST `/`
Accepts form fields to filter results, returning a rendered HTML table (max 100 rows):

Form fields (all optional):
- `bin_number` (exact match)
- `country` (exact match via UI; server uses `=` in `app.py` but LIKE is used in `query_data.py` helper)
- `bank_name` (exact match via UI)
- `card_name` (exact match via UI)
- `card_type` (exact match)
- `provider_type` (exact match)
- `time_update` (substring match)
- `note` (substring match)

Example form POST (returns HTML):
```bash
curl -s -X POST \
  -F "country=UNITED STATES" \
  -F "provider_type=PERSONAL" \
  http://localhost:5000/ > results.html
open results.html  # or xdg-open results.html
```

Notes:
- This endpoint renders HTML, not JSON. For programmatic access to data, prefer the Python helper `query_data.query_bin` documented in the Python Modules section.
- A `LIMIT 100` is applied to protect the application.
