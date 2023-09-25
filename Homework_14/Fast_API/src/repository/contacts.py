from typing import Type
from datetime import datetime, timedelta
from fastapi import HTTPException, status
from sqlalchemy import text, and_
from sqlalchemy.orm import Session

from src.database.models import Contact, User
from schemas import ContactRequest




async def create_contact(contact: ContactRequest, db: Session, current_user: User) -> Contact:
    """
    Retrieves a list of notes for a specific user with specified pagination parameters.

    :param contact: Data for the created contact.
    :type contact: NoteModel
    :param db: The database session.
    :type db: Session
    :param current_user: creates a contact for the user.
    :type current_user: User
    :return: Creates a contact for a specific user.
    :rtype: Contact
    """
    if db.query(Contact).filter(and_(Contact.phone_number == contact.phone_number, Contact.user_id == current_user.id)).first():
        raise HTTPException(status_code=400, detail="Phone number already exists")
    
    db_contact = Contact(**contact.model_dump(), user=current_user)
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact


async def get_contact(contact_id: int, db: Session, current_user: User) -> Type[Contact]:
    """
    Gets a contact by contact_id.

    :contact_id: contact id.
    :type contact_id: int
    :param db: The database session.
    :type db: Session
    :param current_user: Gets a contact for the user.
    :type current_user: User
    :return: Gets a contact for a specific user.
    :rtype: Contact
    """
    contact = db.query(Contact).filter(and_(Contact.id == contact_id, Contact.user_id == current_user.id)).first()
    
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


async def get_contacts(db: Session, current_user: User) -> list[Type[Contact]]:
    """
    Gets a contacts.

    :param db: The database session.
    :type db: Session
    :param current_user: Gets a contacts for the user.
    :type current_user: User
    :return: Retrieves contacts for a specific user.
    :rtype: List[Contact]
    """
    contacts = db.query(Contact).filter(Contact.user_id == current_user.id).all()
    return contacts


async def update_contact(contact_id: int, updated_contact: ContactRequest, db: Session, current_user: User) -> Type[Contact]:
    """
    Updates a contact for a user by contact_id.

    :contact_id: contact id.
    :type contact_id: int
    :param updated_contact: Data for the updated contact.
    :type updated_contact: NoteModel
    :param db: The database session.
    :type db: Session
    :param current_user: gets a contact for the user.
    :type current_user: User
    :return: Updates a contact for a specific user.
    :rtype: Contact
    """
    contact = db.query(Contact).filter(and_(Contact.id == contact_id, Contact.user_id == current_user.id)).first()
    
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")

    for attr, value in updated_contact.model_dump().items():
        setattr(contact, attr, value)

    db.commit()
    db.refresh(contact)
    return contact


async def delete_contact(contact_id: int, db: Session, current_user: User) -> Type[Contact]:
    """
    Delete a contact for a user by contact_id.

    :contact_id: contact id.
    :type contact_id: int
    :param db: The database session.
    :type db: Session
    :param current_user: gets a contact for the user.
    :type current_user: User
    :return: Deletes a contact for a specific user.
    :rtype: Contact
    """
    contact = db.query(Contact).filter(and_(Contact.id == contact_id, Contact.user_id == current_user.id)).first()
    
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    
    db.delete(contact)
    db.commit()
    return contact


async def search_contacts(q: str, skip: int, limit: int, db: Session, current_user: User) -> list[Type[Contact]]:
    """
    Searches for contacts for a specific user with the specified pagination options.

    :param q: Search parameter.
    :type q: str
    :param skip: The number of contacts to skip.
    :type skip: int
    :param limit: The maximum number of contacts to return.
    :type limit: int
    :param db: The database session.
    :type db: Session
    :param current_user: search a contacts for the user.
    :type current_user: User
    :return: Searches for contacts for a specific user.
    :rtype: List[Contact]
    """
    contacts = db.query(Contact).filter(and_(
        (Contact.first_name.ilike(f"%{q}%")
         | Contact.last_name.ilike(f"%{q}%")
         | Contact.email.ilike(f"%{q}%")), Contact.user_id == current_user.id)
    ).offset(skip).limit(limit).all()
    return contacts


async def upcoming_birthdays(db: Session, current_user: User) -> list[Type[Contact]]:
    """
    Shows upcoming birthdays for contacts 7 days in advance.

    :param db: The database session.
    :type db: Session
    :param current_user: gets a birthdays for the users.
    :type current_user: User
    :return: We get the nearest birthdays for contacts.
    :rtype: List[Contact]
    """
    today = datetime.today()
    seven_days_later = today + timedelta(days=7)
    upcoming_birthdays_this_year = db.query(Contact).filter(
        and_(text("TO_CHAR(birthday, 'MM-DD') BETWEEN :start_date AND :end_date"),
             Contact.user_id == current_user.id)).params(start_date=today.strftime('%m-%d'), end_date=seven_days_later.strftime('%m-%d')).all()
    return upcoming_birthdays_this_year
