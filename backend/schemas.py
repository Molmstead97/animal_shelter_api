from pydantic import BaseModel

class Shelter(BaseModel):
    name: str
    address: str
    animals: dict[str, str]
    

        

    