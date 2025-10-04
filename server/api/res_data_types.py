from typing import Optional, List

from api.resp_orm_models import __BaseModelWithConfig
from api.resp_orm_models import SpyCat, MissionCompact, MissionExtended, MissionTarget


class MessageResponse(__BaseModelWithConfig):
    message: str


class SuccessResponse(__BaseModelWithConfig):
    success: bool


class GetSpyCatsResp(__BaseModelWithConfig):
    cats: List[SpyCat]


class GetMissionsResp(__BaseModelWithConfig):
    missions: List[MissionCompact]
