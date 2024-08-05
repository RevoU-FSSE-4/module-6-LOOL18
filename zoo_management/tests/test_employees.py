def test_get_employees(client):
    response = client.get("/employees")
    assert response.status_code == 200

def test_add_employee(client):
    response = client.post("/employees", json={
        "name": "John Doe",
        "email": "john@example.com",
        "phone_number": "1234567890",
        "role": "Keeper",
        "schedule": "9am-5pm"
    })
    assert response.status_code == 201
    assert response.json['name'] == "John Doe"
