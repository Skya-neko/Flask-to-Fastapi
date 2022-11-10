from fastapi import APIRouter
from ..models.CustomerService import *

router = APIRouter()
service = CustomerService.getInstance();

@router.get('/endpoint1')
def getAdsData():
    return 'Welcome to Test'

@router.get('/customers')
def getCustomer(id):
    return service.getCustomers()

@router.get('/customer/{id}')
def getPersonalData(id):
    return service.getCustomerById(id)

