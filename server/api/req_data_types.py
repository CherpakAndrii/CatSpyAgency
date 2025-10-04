from typing import List

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

class CreateTargetData(__BaseModelWithConfig):
    name: str
    country: str

class CreateMissionData(__BaseModelWithConfig):
    targets: List[CreateTargetData]

class AssignSpyCatData(__BaseModelWithConfig):
    cat_id: int

class CreateNoteData(__BaseModelWithConfig):
    text: str
