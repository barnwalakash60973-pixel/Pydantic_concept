from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated


 #field_validater -> if any one value in str then change in number. like '30' -> 30



class Patient(BaseModel):

    name: str
    email: EmailStr  
    age: int 
    weight: float
    married: bool
    allergies: Optional[List[str]]  = None
    contact_details: Optional[Dict[str, str]] = None

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains = ['hdfc.com', 'icic.com'] 
        #abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:        #if other email write then error give
            raise ValueError('Not a valid domain')
        
        return value
    

    @field_validator('name')
    @classmethod
    def transform_name(cls, value):  #it's return name in upper letter
        return value.upper()


def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('updated')


Patient_info = {'name':'akash', 'email':'abc@icic.com'
                , 'age':20,'weight':49, 'married': False}

patient1 = Patient(**Patient_info)

update_patient_data(patient1)