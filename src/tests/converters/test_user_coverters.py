from src.infra.converters.users import (
    user_from_entity,
    user_to_entity,
)
from src.domain.entities.users import User as UserEntity
from src.infra.database.models.users import User as UserModel


def test_user_to_entity(user_model: UserModel, user_entity: UserEntity):
    converted_entity = user_to_entity(user_model)

    assert converted_entity.user_id == user_entity.user_id, f"{converted_entity.user_id=}"
    assert converted_entity.telegram_id == user_entity.telegram_id, f"{converted_entity.telegram_id=}"
    assert converted_entity.name == user_entity.name, f"{converted_entity.name=}"


def test_user_from_entity(user_entity: UserEntity, user_model: UserModel):
    converted_model = user_from_entity(user_entity)

    assert converted_model.id == user_model.id, f"{converted_model.id=}"
    assert converted_model.telegram_id == user_model.telegram_id, f"{converted_model.telegram_id=}"
    assert converted_model.name == user_model.name, f"{converted_model.name=}"
