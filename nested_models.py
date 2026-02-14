from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'Giridih', 'state':'Jharkhand', 'pin':'815310'}

address1 = Address(**address_dict)

patient_dict = {'name':'akash', 'gender':'male', 'age':20, 'address':address1}

patient = Patient(**patient_dict)

print('The patient details',patient)
print('The patient city is: ',patient.address.city)