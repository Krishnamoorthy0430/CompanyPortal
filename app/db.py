"""Simple in-memory storage for Employee objects.

This module provides thread-safe insert/get/list/update/delete helpers.
No external DB required — data is lost when the process exits.
"""
from typing import Dict, List, Optional
import threading

from app.schemas import Employee

_lock = threading.Lock()
_storage: Dict[int, Employee] = {}
_next_id = 1


def _get_next_id() -> int:
	global _next_id
	with _lock:
		nid = _next_id
		_next_id += 1
		return nid


def insert(data: dict) -> Employee:
	"""Insert a new employee and return the stored Employee (with id)."""
	eid = _get_next_id()
	obj = Employee(id=eid, **data)
	with _lock:
		_storage[eid] = obj
	return obj


def get(employee_id: int) -> Optional[Employee]:
	return _storage.get(employee_id)


def list_all() -> List[Employee]:
	return list(_storage.values())


def update(employee_id: int, fields: dict) -> Optional[Employee]:
	"""Update fields on an existing employee. Returns updated Employee or None."""
	with _lock:
		existing = _storage.get(employee_id)
		if not existing:
			return None
		data = existing.dict()
		data.update({k: v for k, v in fields.items() if v is not None})
		updated = Employee(**data)
		_storage[employee_id] = updated
		return updated


def delete(employee_id: int) -> bool:
	with _lock:
		return _storage.pop(employee_id, None) is not None

