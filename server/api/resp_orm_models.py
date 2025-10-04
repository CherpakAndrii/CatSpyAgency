from typing import Optional, List

from pydantic import BaseModel

class __BaseModelWithConfig(BaseModel):
    class Config:
        validate_assignment = True
        use_enum_values = True


class __BaseModelWithORMConfig(BaseModel):
    class Config:
        validate_assignment = True
        use_enum_values = True
        from_attributes = True


class SpyCat(__BaseModelWithORMConfig):
    cat_id: int
    name: str
    years_of_experience: str
    breed: str
    salary: float



