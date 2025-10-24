from pydantic import EmailStr , AnyUrl , field_validator , Field , BaseModel
from typing import List , Dict , Optional , Annotated
import json
import uuid

# now here we will be defining the base model for our project so that data validation that can be done properly

class Patient(BaseModel):
    id  : str
    name : Annotated[str , Field(max_length=50 , description="Please enter the full name of the patient")]
    email : EmailStr
    age : Annotated[int , Field(..., gt=0 , lt=100 , description="Please enter the patient name")]
    blood_group : str
    diseases : Optional[List[str]] = None
    allergies : Optional[List[str]] = None
    contact_number : Annotated[str , Field(..., min_length=10 , max_length=15 , description="Please enter the patient phone number ")]

# now we arer making a function to add the new patient to our manager

def add_patient():
    try:
        name = input("Enter patient name: ")
        email = input("Enter email of the patient : ")
        age = int(input("Enter age of the patient : "))
        blood_group = input("Enter blood group of the patient : ")
        diseases = input("Enter diseases (comma separated or leave blank): ").split(",")
        allergies = input("Enter allergies (comma separated or leave blank): ").split(",")
        contact_number = input("Enter contact number of the patient : ")

        
        diseases = [d.strip() for d in diseases if d.strip()]
        allergies = [a.strip() for a in allergies if a.strip()]

        # here we r making the patient data on the basis of the above information
        patient_data = {
            "id" : str(uuid.uuid4()),
            "name" : name,
            "email": email,
            "age" : age,
            "blood_group" : blood_group,
            "diseases" : diseases or None,
            "allergies" : allergies or None,
            "contact_number" : contact_number
        }
        # here we will first validate data for the patient before printing it 

        patient_new = Patient(**patient_data)
        save_patient(patient_new)

    except Exception as e:
        print(f"Error occured : {e}")


def save_patient(patient: Patient):
    try:
        # load old data if file exists
        try:
            with open("patients.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        data.append(patient.model_dump())

        with open("patients.json", "w") as f:
            json.dump(data, f, indent=4)

        print(f"\n Patient '{patient.name}' added successfully!")
        print(f" Assigned ID: {patient.id}")

    except Exception as e:
        print(f"Error saving patient: {e}")



if __name__ == "__main__":
    while True:
        print("\n --- Patient Health Record Manager ---")
        print("1. Add new patient")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice. Try again.")

