🏥 Patient Health Record Manager
🚀 A CLI-based Health Record Management System built with Python & Pydantic
📘 Overview

The Patient Health Record Manager is a powerful yet simple command-line application that helps users store, validate, and manage patient details efficiently.

It leverages Pydantic for strict data validation, ensuring every patient entry is accurate and structured, and stores valid records in a patients.json file — making it a lightweight local alternative to complex hospital management systems.

✨ Features

✅ Data Validation with Pydantic
Ensures every record is valid — checks for proper emails, age limits, contact formats, and more.

✅ Automatic Unique Patient ID
Each patient is automatically assigned a globally unique ID using Python’s uuid module.

✅ JSON Storage
All valid patient records are saved in a structured JSON file, making it easy to read, reuse, or integrate into future projects.

✅ Graceful Error Handling
Invalid inputs are caught and explained clearly, ensuring no crashes or corrupted data.

✅ Simple Command-Line Interface (CLI)
Add new patients or exit the system — all through an interactive terminal interface.

🧠 Tech Stack
Component	Description
Language	Python 3.12+
Libraries	pydantic → Data validation
uuid → Unique ID generation
json → Data persistence
⚙️ How It Works

Run the Python script.

Enter patient details — name, email, age, blood group, diseases, allergies, and contact number.

Pydantic validates all the data automatically.

If valid ✅ → A new patient entry is added to patients.json.

If invalid ❌ → The app explains what went wrong and lets you try again
