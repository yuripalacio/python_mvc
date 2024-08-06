import pytest
from .person_creator_controller import PersonCreatorController

class MockPeopleRepository:
  def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int):
    pass

def test_create():
  person_infos = {
    "first_name": "Jhon",
    "last_name": "Doe",
    "age": 31,
    "pet_id": 5
  }

  controller = PersonCreatorController(MockPeopleRepository())
  response = controller.create(person_info=person_infos)

  assert response["data"]["type"] == "Person"
  assert response["data"]["count"] == 1
  assert response["data"]["attributes"] == person_infos

def test_create_error():
  person_infos = {
    "first_name": "Jhon",
    "last_name": "Doe 2",
    "age": 31,
    "pet_id": 5
  }

  controller = PersonCreatorController(MockPeopleRepository())
  with pytest.raises(Exception):
    controller.create(person_info=person_infos)
