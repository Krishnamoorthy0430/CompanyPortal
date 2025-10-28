from pydantic import BaseModel, EmailStr
from typing import Optional


class EmployeeBase(BaseModel):
	name: str
	email: Optional[EmailStr] = None
	department: Optional[str] = None
	is_active: bool = True


class EmployeeCreate(EmployeeBase):
	"""Model used when creating a new employee (id assigned server-side)."""
	pass


class EmployeeUpdate(BaseModel):
	name: Optional[str] = None
	email: Optional[EmailStr] = None
	department: Optional[str] = None
	is_active: Optional[bool] = None


class Employee(EmployeeBase):
	id: int

	class Config:
		from_attributes = True

