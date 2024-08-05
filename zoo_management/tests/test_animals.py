def test_get_animals(client):
    response = client.get("/animals")
    assert response.status_code == 200

def test_add_animal(client):
    response = client.post("/animals", json={
        "species": "Lion",
        "age": 5,
        "gender": "Male",
        "special_requirements": "None"
    })
    assert response.status_code == 201
    assert response.json['species'] == "Lion"
