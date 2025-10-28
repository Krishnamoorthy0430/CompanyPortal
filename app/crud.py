from typing import List, Optional
from app import db
from app.schemas import EmployeeCreate, EmployeeUpdate, Employee


def create_employee(payload: EmployeeCreate) -> Employee:
	"""Create and store a new employee."""
	data = payload.dict()
	return db.insert(data)


def get_employee(employee_id: int) -> Optional[Employee]:
	return db.get(employee_id)


def list_employees() -> List[Employee]:
	return db.list_all()


def update_employee(employee_id: int, payload: EmployeeUpdate) -> Optional[Employee]:
	return db.update(employee_id, payload.dict())


def delete_employee(employee_id: int) -> bool:
	return db.delete(employee_id)

