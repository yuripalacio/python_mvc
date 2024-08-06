from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface

class PetDeleterController:
  def __init__(self, pet_repository: PetsRepositoryInterface) -> None:
    self.__pets_repository = pet_repository

  def delete(self, name: str) -> None:
    self.__pets_repository.delete_pets(name)
