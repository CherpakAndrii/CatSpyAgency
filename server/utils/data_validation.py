from requests import get

from constants import BREED_VALIDATION_ENDPOINT, MAX_SALARY
from utils.logging_utils import logger

def validate_breed(breed: str) -> bool:
    response = get(BREED_VALIDATION_ENDPOINT)
    if response.status_code == 200:
        data = response.json()
        breeds = {br.get('name', '').lower() for br in data}

        return breed.lower() in breeds
    elif response.status_code == 500:
        return False
    else:
        logger.error(f"Error: {response.status_code}")


def validate_salary(salary: float) -> bool:
    return 0 < salary <= MAX_SALARY