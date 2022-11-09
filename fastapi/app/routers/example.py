from fastapi import APIRouter
from ..models.customer import *
router = APIRouter()


@router.get('/endpoint1')
def getAdsData():
    return 'welcome to test'

@router.get('/customer/{id}')
def getPersonalData():
    page = customer(con)
    jsonData = page.select_info()
    return jsonData

