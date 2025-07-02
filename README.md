# COBOL Payload Generator

This tool automates the extraction and transformation of COBOL copybook structures into structured JSON payloads. It is designed to assist in generating RESTful interface definitions by reading COBOL programs, resolving their copybooks, and optionally filtering with sample XML files.

---

## 🧩 Features

- Parses COBOL `COPY` statements recursively
- Supports nested copybooks
- Generates structured payloads based on field hierarchies
- Optionally filters fields based on sample XML files
- Outputs to CSV and optionally to a database (MySQL, PostgreSQL, SQLite)
- Auto-converts COBOL field names to camelCase
- Detects copybooks used within the LINKAGE SECTION

---

