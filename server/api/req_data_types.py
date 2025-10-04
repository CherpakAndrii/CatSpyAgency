from pydantic import BaseModel

class __BaseModelWithConfig(BaseModel):
    class Config:
        validate_assignment = True


class CreateSpyCatData(__BaseModelWithConfig):
    name: str
    years_of_experience: float
    breed: str
    salary: float

class UpdateCatSalaryData(__BaseModelWithConfig):
    salary: float
