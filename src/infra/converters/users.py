from src.domain.entities.users import User as UserEntity
from src.infra.database.models.users import User as UserModel


def user_to_entity(user: UserModel) -> UserEntity:
    return UserEntity(
        user_id=user.id,
        telegram_id=user.telegram_id,
        name=user.name,
    )


def user_from_entity(entity: UserEntity) -> UserModel:
    return UserModel(
        id=entity.user_id,
        telegram_id=entity.telegram_id,
        name=entity.name,
    )
