from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict, Optional


#computed_field -> when it don't take through users it calculated the value through your software

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float #kgs
    hieght: float # meter
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]


    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.hieght**2), 2)
        return bmi
    


def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('BMI: ',patient.bmi)
    print('updated')

    
Patient_info = {
    'name': 'akash',
    'email': 'abc@icic.com',
    'age': 20,
    'weight': 49,
    'hieght': 1.21,
    'married': False,
    'contact_details': {'phone': '879703'}
}

patient1 = Patient(**Patient_info)

update_patient_data(patient1)
