from .pet_deleter_controller import PetDeleterController

def test_delete_pet(mocker):
  mocker_repository = mocker.Mock()
  controller = PetDeleterController(mocker_repository)
  controller.delete("rex")

  mocker_repository.delete_pets.assert_called_once_with("rex")
