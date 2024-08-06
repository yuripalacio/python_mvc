from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController

class MockPetsRepository:
  def list_pets(self):
    return [
      PetsTable(
        name="Rex",
        type="Dog",
        id=2
      ),
      PetsTable(
        name="Bob",
        type="Dog",
        id=4
      )
    ]

def test_list_pets():
  controller = PetListerController(MockPetsRepository())
  response = controller.list()

  expected_response = {
    "data": {
        "type": "Pets",
        "count": 2,
        "attributes": [
          { "name": "Rex", "type": "Dog", "id": 2 },
          { "name": "Bob", "type": "Dog", "id": 4 }
        ]
      }
  }

  assert response == expected_response
