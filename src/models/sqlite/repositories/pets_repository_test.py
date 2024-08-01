from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.pets import PetsTable
from .pets_repository import PetsRepository

class MockConnection:
  def __init__(self) -> None:
    self.session = UnifiedAlchemyMagicMock(
      data=[
        (
          [mock.call.query(PetsTable)], #query
          [
            PetsTable(name="dog", type="dog"),
            PetsTable(name="cat", type="cat")
          ] #result
        )
      ]
    )

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    pass

def test_list_pets():
  mock_connection = MockConnection()
  repo = PetsRepository(mock_connection)
  response = repo.list_pets()

  mock_connection.session.query.assert_called_once_with(PetsTable)
  mock_connection.session.all.asert_called_once()
  mock_connection.session.filter.assert_not_called()

  assert response[0].name == "dog"
