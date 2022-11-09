from fastapi import APIRouter

router = APIRouter()


@router.get('/endpoint1')
def getAdsData():
    return 'welcome to test'
