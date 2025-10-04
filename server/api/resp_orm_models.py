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
    years_of_experience: float
    breed: str
    salary: float


class MissionCompact(__BaseModelWithORMConfig):
    mission_id: int
    cat_id: int
    is_completed: bool


class TargetNotes(__BaseModelWithORMConfig):
    note_id: int
    text: str
    target_id: int


class MissionTarget(__BaseModelWithORMConfig):
    target_id: int
    name: str
    country: str
    is_completed: bool
    mission_id: int
    notes: Optional[List[TargetNotes]] = None


class MissionExtended(__BaseModelWithORMConfig):
    mission_id: int
    cat_id: int
    is_completed: bool
    targets: List[MissionTarget]
    spy_cat: Optional[SpyCat] = None



