# Frontend (Templates & JavaScript)

The frontend is a minimal Bootstrap + jQuery app with Select2-enhanced dropdowns.

## Templates

### `templates/index.html`
- Renders the main search form.
- Fields:
  - `bin_number` (text)
  - `country` (Select2, populated by `/get_options`)
  - `bank_name` (Select2, populated by `/get_options`)
  - `card_name` (Select2, populated by `/get_options`)
  - `card_type` (Select2, populated by `/get_options`)
  - `provider_type` (Select2, populated by `/get_options`)
  - `time_update` (text, freeform, partial match)
  - `note` (text, freeform, partial match)
- Submits a `POST` to `/`.

### `templates/results.html`
- Displays search results as a table with headers:
  `BIN Number, Country, Bank Name, Card Name, Card Type, Provider Type, Base, Time Update, Note`.
- Includes a back button to return to `/`.

## Static Assets

### `static/js/script.js`
- On document ready:
  - Initializes Select2 on all `.select2` elements.
  - Performs `GET /get_options` and populates the `country`, `bank_name`, `card_name`, `card_type`, and `provider_type` dropdowns with the returned list values.

### `static/css/style.css`
- Adds light theming, spacing, and Select2 sizing adjustments.

## Example: How dropdowns are populated
```javascript
$.ajax({
  url: '/get_options',
  method: 'GET',
  success: function (data) {
    $('#country').append(new Option('Example', 'Example'));
    // Similar for bank_name, card_name, card_type, provider_type
  }
});
```
