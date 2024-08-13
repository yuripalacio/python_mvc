from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pets_repository import PetsRepository
from src.controllers.pet_lister_controller import PetListerController
from src.views.pet_lister_view import PetListerView

def pet_lister_composer():
  model = PetsRepository(db_connection=db_connection_handler)
  controller = PetListerController(pet_repository=model)
  view = PetListerView(controller=controller)

  return view
