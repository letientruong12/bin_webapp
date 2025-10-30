# Database Schema & Indexes

SQLite database file: `bin_database.db`.

## Table: `bin_data`
Columns:
- `bin_number INTEGER`
- `country TEXT`
- `bank_name TEXT`
- `card_name TEXT`
- `card_type TEXT`
- `provider_type TEXT`
- `base TEXT`
- `time_update TEXT`
- `note TEXT`

## Indexes
Created by `create_indexes.py`:
- `CREATE INDEX IF NOT EXISTS idx_bin_number ON bin_data(bin_number)`
- `CREATE INDEX IF NOT EXISTS idx_country ON bin_data(country)`
- `CREATE INDEX IF NOT EXISTS idx_bank_name ON bin_data(bank_name)`
- `CREATE INDEX IF NOT EXISTS idx_card_type ON bin_data(card_type)`
- `CREATE INDEX IF NOT EXISTS idx_provider_type ON bin_data(provider_type)`
- `CREATE INDEX IF NOT EXISTS idx_time_update ON bin_data(time_update)`

## Notes
- The application uses simple parameterized queries for safety and adds `LIMIT 100` to UI queries.
- Consider normalizing frequently repeated strings (e.g., `country`, `bank_name`) in a future evolution for space/perf trade-offs.
