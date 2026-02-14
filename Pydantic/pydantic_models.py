from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated


 #in Pydantic model all are value need to pass if you want any value not
   #then also run then you use optional that data and assign None

#Field used on all case str as well as int float. 

class Patient(BaseModel):

    name: Annotated[str, Field(max_length = 30, title = 'Name of the patient', description = 
    'Give the patient name in less than 30 characters', examples = ['Akash', 'SiKalicharan'])] 

    email: EmailStr  

    linkedin_url: AnyUrl

    age: int = Field(gt=0,lt=60)  #age between 0 to 60 else gives error

    weight: Annotated[float,Field(gt = 0,strict = True)]  #strict = True -> means weight must in float or int

    married: Annotated[bool, Field(default = None,description = 'Is the patient married or not')]

    allergies: Optional[List[str]]  = None

    contact_details: Optional[Dict[str,str]] = None

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)

    print('inserted')


def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print('updated')


Patient_info = {'name':'Akash', 'email':'abc@gmail.com', 'linkedin_url':'https://linkedin.com/1332'
                , 'age':20, 'weight':49, 'married': False}

patient1 = Patient(**Patient_info)

update_patient_data(patient1)