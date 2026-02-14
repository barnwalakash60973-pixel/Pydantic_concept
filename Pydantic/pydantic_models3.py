from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict, Optional

#model_validater -> it's convert multiple data instead of single str to number -> like '12' to 12

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    @model_validator(mode="after")
    def validate_emergency_contact(self):
        if self.age > 60 and 'emergency' not in self.contact_details:
            raise ValueError(
                'Patients older than 60 must have an emergency contact'
            )
        return self
    


def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('updated')

    
Patient_info = {
    'name': 'akash',
    'email': 'abc@gmail.com',
    'age': '65',
    'weight': 49,
    'married': False,
    'contact_details': {'phone': '879703', 'emergency':'231232'}}


patient1 = Patient(**Patient_info)

update_patient_data(patient1)
