from fastapi import APIRouter, Request, HTTPException

from database.sqlite_connector import Session
from api.req_data_types import CreateMissionData, AssignSpyCatData
from database.models import Mission, SpyCat, MissionTarget
from api.res_data_types import GetMissionsResp, MissionExtended

missions_router = APIRouter()

@missions_router.get('/', response_model=GetMissionsResp)
def get_missions():
    with Session() as session:
        missions = session.query(Mission).all()
        missions_list = [mission.to_dict() for mission in missions]
        return {'missions': missions_list}


@missions_router.get('/{mission_id}', response_model=MissionExtended)
def get_mission(mission_id: int):
    with Session() as session:
        mission = session.query(Mission).get(mission_id)
        if mission is None:
            raise HTTPException(status_code=404, detail="Mission not found")
        return mission.to_extended_dict()


@missions_router.post('/', response_model=GetMissionsResp)
def create_mission(data: CreateMissionData):
    session = Session()

    if not (1 <= len(data.targets) <= 3):
        raise HTTPException(status_code=400, detail="Invalid amount of targets")

    # Actually should validate all the other fields, but not as a test assignment

    new_mission = Mission()
    session.add(new_mission)
    session.commit()
    for target_data in data.targets:
        target = MissionTarget(name=target_data.name, country=target_data.country, mission_id=new_mission.mission_id)
        session.add(target)
    session.commit()

    missions = session.query(Mission).all()
    mission_list = [mission.to_dict() for mission in missions]
    session.close()
    return {'missions': mission_list}


@missions_router.put('/{mission_id}', response_model=GetMissionsResp)
def assign_cat(data: AssignSpyCatData, mission_id: int):
    session = Session()

    mission = session.query(Mission).get(mission_id)
    if mission is None:
        session.close()
        raise HTTPException(status_code=404, detail="Mission not found")

    cat = session.query(SpyCat).get(data.cat_id)
    if cat is None:
        session.close()
        raise HTTPException(status_code=404, detail="Cat not found")

    mission.cat_id = data.cat_id
    session.commit()
    missions = session.query(Mission).all()
    mission_list = [cat.to_dict() for cat in missions]
    session.close()
    return {'missions': mission_list}


@missions_router.delete('/{mission_id}', response_model=GetMissionsResp)
def delete_mission(mission_id: int):
    session = Session()

    mission = session.query(Mission).get(mission_id)
    if mission is None:
        session.close()
        raise HTTPException(status_code=404, detail="Mission not found")

    if mission.cat_id is not None:
        session.close()
        raise HTTPException(status_code=403, detail="Mission is already assigned, it cannot be deleted")

    session.delete(mission)
    session.commit()
    missions = session.query(Mission).all()
    missions_list = [mission.to_dict() for mission in missions]
    session.close()
    return {'missions': missions_list}
