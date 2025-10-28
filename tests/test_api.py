from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
def test_crud_employee():
	# create
	payload = {"name": "Alice", "email": "alice@example.com", "department": "Engineering"}
	r = client.post("/employees", json=payload)
	assert r.status_code == 201
	created = r.json()
	assert created["name"] == "Alice"
	eid = created["id"]

	# get
	r = client.get(f"/employees/{eid}")
	assert r.status_code == 200
	assert r.json()["email"] == "alice@example.com"

	# list
	r = client.get("/employees")
	assert r.status_code == 200
	assert isinstance(r.json(), list)

	# update
	r = client.put(f"/employees/{eid}", json={"department": "Product"})
	assert r.status_code == 200
	assert r.json()["department"] == "Product"

	# delete
	r = client.delete(f"/employees/{eid}")
	assert r.status_code == 204

	# not found after delete
	r = client.get(f"/employees/{eid}")
	assert r.status_code == 404
