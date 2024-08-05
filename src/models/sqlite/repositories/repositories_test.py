import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository
from .people_repository import PeopleRepository

# db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="database interation")
def test_list_pets():
  repo = PetsRepository(db_connection_handler)
  response = repo.list_pets()
  print(response)

@pytest.mark.skip(reason="database interation")
def test_delete_pet():
  name = "belinha"
  repo = PetsRepository(db_connection_handler)
  repo.delete_pets(name)

@pytest.mark.skip(reason="database interation")
def test_insert_person():
  first_name = "name"
  last_name = "last name"
  age = 31
  pet_id = 2

  repo = PeopleRepository(db_connection_handler)
  repo.insert_person(first_name, last_name, age, pet_id)

@pytest.mark.skip(reason="database interation")
def test_get_person():
  person_id = 1

  repo = PeopleRepository(db_connection_handler)
  response = repo.get_person(person_id)
  print(response)
