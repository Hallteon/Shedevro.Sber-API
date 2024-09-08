from datetime import datetime
from typing import Optional, List

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from api.database import Base
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy import (Column, Integer, String, TIMESTAMP, ForeignKey,
                        Boolean, Text, DATE, Table)


class Role(Base):
    __tablename__ = 'role'

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String, unique=True, nullable=False)
    role_type: Mapped[str] = Column(String, unique=True, nullable=False)
    users: Mapped[Optional[List['User']]] = relationship('User', back_populates='role')

    def __str__(self):
        return self.name


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'user'

    id: Mapped[int] = Column(Integer, primary_key=True)
    email: Mapped[str] = Column(String, unique=True, nullable=False)
    lastname: Mapped[str] = Column(String, nullable=False)
    firstname: Mapped[str] = Column(String, nullable=False)
    surname: Mapped[str] = Column(String, nullable=False)

    registered_at: Mapped[datetime] = Column(TIMESTAMP, default=datetime.utcnow)

    role_id: Mapped[int] = Column(Integer, ForeignKey('role.id'), nullable=True)
    role: Mapped[Optional['Role']] = relationship('Role', back_populates='users')

    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
