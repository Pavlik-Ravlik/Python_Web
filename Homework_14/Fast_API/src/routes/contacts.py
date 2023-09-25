from typing import List
from fastapi import Depends, Query, APIRouter, status
from sqlalchemy.orm import Session
from src.database.models import User
from schemas import ContactRequest, ContactResponse
from src.database.db import get_db
from src.repository import contacts as repository_contacts
from src.services.auth import auth_service
from fastapi_limiter.depends import RateLimiter


router = APIRouter(prefix="", tags=['contacts'])


@router.post("/", response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
async def create_contact(contact: ContactRequest, db: Session = Depends(get_db), current_user: User = Depends(auth_service.get_current_user)):
    """
    Function for creating a contact.

    :param contact: Data for the created contact.
    :type contact: NoteModel
    :param db: The database session.
    :type db: Session
    :param current_user: creates a contact for the user.
    :type current_user: User
    :return: Creates a contact.
    :rtype: Contact
    """
    contact = await repository_contacts.create_contact(contact, db, current_user)
    return contact


@router.get("/", response_model=List[ContactResponse], description='No more than 10 requests per minute', dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def read_contacts(db: Session = Depends(get_db), current_user: User = Depends(auth_service.get_current_user)):
    """
    Function for read a contacts.

    :param db: The database session.
    :type db: Session
    :param current_user: creates a contact for the user.
    :type current_user: User
    :return: Read a contacts for a specific user.
    :rtype: Contacts
    """
    contacts = await repository_contacts.get_contacts(db, current_user)
    return contacts


@router.get("/{contact_id}", response_model=ContactResponse)
async def read_contact(contact_id: int, db: Session = Depends(get_db), current_user: User = Depends(auth_service.get_current_user)):
    """
    Function for read a contact.

    :param contact_id: Contact ID
    type contact_id: int
    :param db: The database session.
    :type db: Session
    :param current_user: creates a contact for the user.
    :type current_user: User
    :return: Read a contact for a specific user.
    :rtype: Contact
    """
    contact = await repository_contacts.get_contact(contact_id, db, current_user)
    return contact


@router.put("/{contact_id}", response_model=ContactResponse)
async def update_contact(contact_id: int, updated_contact: ContactRequest, db: Session = Depends(get_db), current_user: User = Depends(auth_service.get_current_user)):
    """
    Function for update a contact.

    :param contact_id: Contact ID
    type contact_id: int
    :param updated_contact: Data for the updated contact.
    :type contact: NoteModel
    :param db: The database session.
    :type db: Session
    :param current_user: updates a contact for the user.
    :type current_user: User
    :return: Update a contact for a specific user.
    :rtype: Contact
    """
    contact = await repository_contacts.update_contact(contact_id, updated_contact, db, current_user)
    return contact


@router.delete("/{contact_id}", response_model=ContactResponse)
async def delete_contact(contact_id: int, db: Session = Depends(get_db), current_user: User = Depends(auth_service.get_current_user)):
    """
    Function for delete a contact.

    :param contact_id: Contact ID
    :type contact_id: int
    :param db: The database session.
    :type db: Session
    :param current_user: deletes a contact for the user.
    :type current_user: User
    :return: Delete a contact for a specific user.
    :rtype: Contact
    """
    contact = await repository_contacts.delete_contact(contact_id, db, current_user)
    return contact


@router.get("/search", response_model=List[ContactResponse])
async def search_contacts(q: str = Query(..., description="Search query for name, last name, or email"), skip: int = 0, limit: int = 10, db: Session = Depends(get_db),
        current_user: User = Depends(auth_service.get_current_user)
):
    """
    Function for search a contacts.

    :param q: Search option
    :type q: str
    :param skip: The number of notes to skip.
    :type skip: int
    :param limit: The maximum number of notes to return.
    :type limit: int
    :param db: The database session
    :type db: Session
    :param current_user: search a contacts for the user.
    :type current_user: User
    :return: Search a contacts for a param skip and limit.
    :rtype: Contacts
    """
    contacts = await repository_contacts.search_contacts(q, skip, limit, db, current_user)
    return contacts


@router.get("/birthdays/", response_model=List[ContactResponse])
async def upcoming_birthdays(db: Session = Depends(get_db), current_user: User = Depends(auth_service.get_current_user)):
    """
    Function for to represent upcoming birthdays.

    :param db: The database session
    :type db: Session
    :param current_user: creates a contact for the user.
    :type current_user: User
    :return: Upcoming birthdays a contacts for a param skip and limit.
    :rtype: Contacts
    """
    upcoming_birthdays_this_year = await repository_contacts.upcoming_birthdays(db, current_user)
    return upcoming_birthdays_this_year
