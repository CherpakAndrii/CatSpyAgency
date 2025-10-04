from fastapi import APIRouter, Request, HTTPException

from database.sqlite_connector import Session
from api.req_data_types import CreateNoteData
from database.models import MissionTarget, TargetNote
from api.res_data_types import MissionTarget as MissionTargetResp

targets_router = APIRouter()

@targets_router.get('/{target_id}', response_model=MissionTargetResp)
def get_target_notes(target_id: int):
    with Session() as session:
        target = session.query(MissionTarget).get(target_id)
        if target is None:
            raise HTTPException(status_code=404, detail="Target not found")
        return target.to_extended_dict()


@targets_router.put('/{target_id}', response_model=MissionTargetResp)
def mark_target_as_complete(target_id: int):
    session = Session()

    target = session.query(MissionTarget).get(target_id)
    if target is None:
        session.close()
        raise HTTPException(status_code=404, detail="Target not found")
    if target.is_completed > 0:
        session.close()
        raise HTTPException(status_code=403, detail="Target is already complete")

    if len(target.notes) < 1:
        raise HTTPException(status_code=403, detail="Cannot complete without notes")

    target.is_completed = 1
    session.commit()

    target_data = session.query(MissionTarget).get(target_id).to_extended_dict()
    session.close()
    return target_data


@targets_router.post('/{target_id}', response_model=MissionTargetResp)
def create_note(target_id: int, data: CreateNoteData):
    session = Session()

    target = session.query(MissionTarget).get(target_id)
    if target is None:
        session.close()
        raise HTTPException(status_code=404, detail="Target not found")
    if target.is_completed > 0:
        session.close()
        raise HTTPException(status_code=403, detail="Target is complete, cannot add notes")

    if not (1 <= len(data.text) <= 500):
        raise HTTPException(status_code=400, detail="Invalid note length")

    new_note = TargetNote(target_id=target_id, text=data.text)
    session.add(new_note)
    session.commit()

    target_data = session.query(MissionTarget).get(target_id).to_extended_dict()
    session.close()
    return target_data


@targets_router.put('/notes/{note_id}', response_model=MissionTargetResp)
def edit_note(data: CreateNoteData, note_id: int):
    session = Session()

    note = session.query(TargetNote).get(note_id)
    if note is None:
        session.close()
        raise HTTPException(status_code=404, detail="Note not found")
    target = note.target
    if target is None:
        session.close()
        raise HTTPException(status_code=404, detail="Target not found")
    if target.is_completed > 0:
        session.close()
        raise HTTPException(status_code=403, detail="Target is complete, cannot edit notes")

    if not (1 <= len(data.text) <= 500):
        raise HTTPException(status_code=400, detail="Invalid note length")

    note.text = data.text
    session.commit()

    target_data = session.query(TargetNote).get(note_id).target.to_extended_dict()
    session.close()
    return target_data


@targets_router.delete('/notes/{note_id}', response_model=MissionTargetResp)
def delete_note(note_id: int):
    session = Session()

    note = session.query(TargetNote).get(note_id)
    if note is None:
        session.close()
        raise HTTPException(status_code=404, detail="Note not found")
    target = note.target
    if target is None:
        session.close()
        raise HTTPException(status_code=404, detail="Target not found")
    if target.is_completed > 0:
        session.close()
        raise HTTPException(status_code=403, detail="Target is complete, cannot edit notes")

    session.delete(note)
    session.commit()

    target_data = target.to_extended_dict()
    session.close()
    return target_data
