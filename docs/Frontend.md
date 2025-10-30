# Frontend Components

This document describes the HTML templates, JavaScript, and CSS used by the app.

## Pages

### `templates/index.html`
- Renders the search form with the following fields:
  - `bin_number` (text)
  - `country` (select; Select2-enhanced)
  - `bank_name` (select; Select2-enhanced)
  - `card_name` (select; Select2-enhanced)
  - `card_type` (select; Select2-enhanced)
  - `provider_type` (select; Select2-enhanced)
  - `time_update` (text, e.g., `YYYY-MM-DD`)
  - `note` (text)
- Dependencies loaded from CDN:
  - Bootstrap 5.3.2 (CSS/JS)
  - jQuery 3.6.0
  - Select2 4.1.0-rc.0
- Custom assets:
  - `/static/css/style.css`
  - `/static/js/script.js`

### `templates/results.html`
- Displays a table of results (up to 100 rows) with columns:
  `BIN Number, Country, Bank Name, Card Name, Card Type, Provider Type, Base, Time Update, Note`.
- Includes a "Back" button to return to `/`.

---

## JavaScript

### `static/js/script.js`
Enhances selects with Select2 and fetches dropdown options from the backend.

- On document ready:
  1. Initializes all elements with class `.select2` using Select2.
  2. Issues `GET /get_options` and appends options to the following selects by ID:
     - `#country`, `#bank_name`, `#card_name`, `#card_type`, `#provider_type`.

- Snippet:
  ```javascript
  $(document).ready(function() {
    $('.select2').select2({ placeholder: 'Chọn giá trị', allowClear: true });

    $.ajax({
      url: '/get_options',
      method: 'GET',
      success: function(data) {
        ['countries','bank_names','card_names','card_types','provider_types'];
        // Populates #country, #bank_name, #card_name, #card_type, #provider_type
      }
    });
  });
  ```

- Customization tips:
  - To pre-select a value: set the `<select>` element’s `value` before initializing Select2.
  - To reload options dynamically (e.g., dependent dropdowns), re-run the append logic after clearing existing options.

---

## CSS

### `static/css/style.css`
Overrides a few Bootstrap defaults and ensures Select2 controls match form height.

- Highlights:
  - Body background: `#f8f9fa`.
  - Form card with subtle shadow.
  - Primary button color tuned for hover/focus.
  - Table cells vertically centered.
  - Select2 styles adjusted to `38px` control height.

---

## End-to-end flow
1. User opens `/` → `index.html` renders form.
2. `script.js` calls `/get_options` and populates dropdowns.
3. User submits form (`POST /`).
4. Server queries SQLite (limited to 100 rows) and returns `results.html`.

---

## Local development
```bash
pip install -r requirements.txt
python app.py  # visit http://localhost:5000
```
