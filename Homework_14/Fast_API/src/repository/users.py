from libgravatar import Gravatar
from sqlalchemy.orm import Session

from src.database.models import User
from schemas import UserModel


async def get_user_by_email(email: str, db: Session) -> User:
    """
    get user by email.

    :param email: Data for the created contact.
    :type email: str
    :param db: The database session.
    :type db: Session
    :return: Get user by email.
    :rtype: User
    """
    return db.query(User).filter(User.email == email).first()


async def create_user(body: UserModel, db: Session) -> User:
    avatar = None
    try:
        g = Gravatar(body.email)
        avatar = g.get_image()
    except Exception as e:
        print(e)
        
    new_user = User(**body.model_dump(), avatar=avatar)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def update_token(user: User, token: str | None, db: Session) -> None:
    user.refresh_token = token
    db.commit()


async def confirmed_email(email: str, db: Session) -> None:
    user = await get_user_by_email(email, db)
    user.confirmed = True
    db.commit()
    