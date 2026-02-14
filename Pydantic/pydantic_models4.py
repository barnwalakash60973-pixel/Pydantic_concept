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


temp = patient.model_dump()  #all data converts in dict form and you can extract the data 
print('The patient details after convert in dict form:\n',temp)
print(type(temp))


temp = patient.model_dump_json(include = ['name','gender'])  #all data converts in json form and you can extrat the data
print("The patient's name and gender:\n",temp)
print(type(temp))