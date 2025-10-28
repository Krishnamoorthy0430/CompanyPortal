from fastapi import APIRouter, HTTPException, status
from typing import List
import logging

from app import crud
from app.schemas import Employee, EmployeeCreate, EmployeeUpdate

router = APIRouter()
logger = logging.getLogger("company_portal.api")


@router.post("/employees", response_model=Employee, status_code=status.HTTP_201_CREATED)
def create_employee(payload: EmployeeCreate):
	logger.info("Creating employee: %s", payload.name)
	emp = crud.create_employee(payload)
	return emp


@router.get("/employees", response_model=List[Employee])
def list_employees():
	logger.info("Listing employees")
	return crud.list_employees()


@router.get("/employees/{employee_id}", response_model=Employee)
def get_employee(employee_id: int):
	emp = crud.get_employee(employee_id)
	if not emp:
		logger.debug("Employee %s not found", employee_id)
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
	return emp


@router.put("/employees/{employee_id}", response_model=Employee)
def update_employee(employee_id: int, payload: EmployeeUpdate):
	updated = crud.update_employee(employee_id, payload)
	if not updated:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
	logger.info("Updated employee %s", employee_id)
	return updated


@router.delete("/employees/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(employee_id: int):
	ok = crud.delete_employee(employee_id)
	if not ok:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
	logger.info("Deleted employee %s", employee_id)
	return None

