from fastapi import APIRouter, Request, HTTPException

from database.sqlite_connector import Session
from api.req_data_types import CreateSpyCatData, UpdateCatSalaryData
from database.models import SpyCat
from api.res_data_types import GetSpyCatsResp, SpyCat as SpyCatResp
from utils.data_validation import validate_breed, validate_salary

spy_cats_router = APIRouter()

@spy_cats_router.get('/', response_model=GetSpyCatsResp)
def get_cats():
    session = Session()
    cats = session.query(SpyCat).all()
    session.close()
    cats_list = [cat.to_dict() for cat in cats]
    return {'cats': cats_list}


@spy_cats_router.get('/{cat_id}', response_model=SpyCatResp)
def get_cat(cat_id: int):
    session = Session()
    cat = session.query(SpyCat).get(cat_id)
    session.close()
    if cat is None:
        raise HTTPException(status_code=404, detail="Cat not found")
    return cat.to_extended_dict()


@spy_cats_router.post('/', response_model=GetSpyCatsResp)
def create_spy_cat(data: CreateSpyCatData):
    session = Session()

    breed_is_valid = validate_breed(data.breed)
    if not breed_is_valid:
        raise HTTPException(status_code=400, detail="Breed is invalid")

    if not validate_salary(data.salary):
        raise HTTPException(status_code=400, detail="Invalid salary")

    # Actually should validate all the other fields, but not as a test assignment

    new_cat = SpyCat(name=data.name, breed=data.breed, years_of_experience=data.years_of_experience, salary=data.salary)
    session.add(new_cat)
    session.commit()
    cats = session.query(SpyCat).all()
    session.close()
    cat_list = [cat.to_dict() for cat in cats]
    return {'cats': cat_list}


@spy_cats_router.put('/{cat_id}', response_model=GetSpyCatsResp)
def update_cat_salary(data: UpdateCatSalaryData, cat_id: int):
    session = Session()

    cat = session.query(SpyCat).get(cat_id)
    if cat is None:
        session.close()
        raise HTTPException(status_code=404, detail="Cat not found")

    if not validate_salary(data.salary):
        raise HTTPException(status_code=400, detail="Invalid salary")

    cat.salary = data.salary
    session.commit()
    cats = session.query(SpyCat).all()
    session.close()
    cat_list = [cat.to_dict() for cat in cats]
    return {'cats': cat_list}


@spy_cats_router.delete('/{cat_id}', response_model=GetSpyCatsResp)
def delete_spy_cat(cat_id: int):
    session = Session()

    cat = session.query(SpyCat).get(cat_id)
    if cat is None:
        session.close()
        raise HTTPException(status_code=404, detail="Cat not found")

    session.delete(cat)
    session.commit()
    cats = session.query(SpyCat).all()
    session.close()
    cats_list = [cat.to_dict() for cat in cats]
    return {'cats': cats_list}
