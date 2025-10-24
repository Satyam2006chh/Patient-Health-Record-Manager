🏥 Patient Health Record Manager
A CLI-based health record management system built with Python and Pydantic.
📘 Overview

The Patient Health Record Manager is a simple yet powerful command-line application that allows users to store, validate, and manage patient details efficiently.

It uses Pydantic for strict data validation (ensuring clean and structured inputs) and stores valid records in a patients.json file — making it a lightweight, local alternative to full-scale hospital management systems.

🚀 Features

✅ Data Validation with Pydantic
Ensures every record is accurate — checks for valid emails, age limits, contact format, and more.

✅ Automatic Unique Patient ID
Each patient is automatically assigned a globally unique ID using Python’s uuid module.

✅ JSON Storage
Stores all valid patient records in a structured JSON file, making it easy to read or use in future applications.

✅ Graceful Error Handling
Catches invalid inputs and informs users about what went wrong — no crashes, no corrupted data.

✅ Simple Command-Line Interface (CLI)
Add new patients or exit the system right from your terminal.

🧠 Tech Stack

Language: Python 3.12+

Libraries:

pydantic → Data validation

uuid → Unique ID generation

json → Data persistence

⚙️ How It Works

Run the Python script.

Enter patient details such as name, email, age, blood group, diseases, allergies, and contact number.

Pydantic validates all the inputs.

If valid, a new patient entry is added to patients.json.

Invalid inputs trigger descriptive error messages for correction.
