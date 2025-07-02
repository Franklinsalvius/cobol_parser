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

## 📁 Project Structure

├── copybooks/ # Folder containing .cpy files
├── XMLS/ # Sample XMLs for filtering (optional)
├── cobol_programs.csv # Input CSV listing COBOL source programs and operations
├── output_payload.csv # Output CSV with generated payloads
├── config.py # Configuration file (DB, folders, flags)
├── main.py # Main script (contains process_and_generate)
└── README.md # You're here
