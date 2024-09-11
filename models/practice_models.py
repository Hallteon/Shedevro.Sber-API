from datetime import datetime
from enum import unique
from typing import Optional, List

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from api.database import Base
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy import (Column, Integer, String, TIMESTAMP, ForeignKey,
                        Boolean, Text, DATE, Table)


class PracticeCategory(Base):
    __tablename__ = 'practice_category'

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String, unique=True, nullable=False)

    practices: Mapped[Optional['Practice']] = relationship('Practice', back_populates='category',
                                                           lazy='selectin')

    def __str__(self):
        return self.name


class Practice(Base):
    __tablename__ = 'practice'

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String, unique=True, nullable=False)
    description: Mapped[str] = Column(Text, unique=True, nullable=False)

    category_id: Mapped[int] = Column(Integer, ForeignKey('practice_category.id'), nullable=True)
    category: Mapped[Optional['PracticeCategory']] = relationship('PracticeCategory', back_populates='practices',
                                                          lazy='selectin')

    company_id: Mapped[int] = Column(Integer, ForeignKey('company.id'), nullable=True)
    company: Mapped[Optional['Company']] = relationship('Company', back_populates='practices',
                                                        lazy='selectin')

    def __str__(self):
        return self.name


class Role(Base):
    __tablename__ = 'role'

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String, unique=True, nullable=False)
    role_type: Mapped[str] = Column(String, unique=True, nullable=False)
    students: Mapped[Optional[List['Student']]] = relationship('Student', back_populates='role', lazy='selectin')
    providers: Mapped[Optional[List['Provider']]] = relationship('Provider', back_populates='role', lazy='selectin')
    companies: Mapped[Optional[List['Company']]] = relationship('Company', back_populates='role', lazy='selectin')

    def __str__(self):
        return self.name


class Category(Base):
    __tablename__ = 'category'

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String, unique=True, nullable=False)
    companies: Mapped[Optional[List['Company']]] = relationship('Company', back_populates='category', lazy='selectin')

    def __str__(self):
        return self.name


class Provider(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'provider'

    id: Mapped[int] = Column(Integer, primary_key=True)
    email: Mapped[str] = Column(String, unique=True, nullable=False)
    name: Mapped[str] = Column(String, unique=True, nullable=False)
    description: Mapped[str] = Column(Text, nullable=True)

    role_id: Mapped[int] = Column(Integer, ForeignKey('role.id'), nullable=True)
    role: Mapped[Optional['Role']] = relationship('Role', back_populates='providers', lazy='selectin')

    students: Mapped[Optional['Student']] = relationship('Student', back_populates='provider',
                                                          lazy='selectin')

    registered_at: Mapped[datetime] = Column(TIMESTAMP, default=datetime.utcnow)
    hashed_password: str = Column(String(length=1024), nullable=False)

    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)

    def __str__(self):
        return self.name


class Company(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'company'

    id: Mapped[int] = Column(Integer, primary_key=True)
    email: Mapped[str] = Column(String, unique=True, nullable=False)
    name: Mapped[str] = Column(String, unique=True, nullable=False)
    description: Mapped[str] = Column(Text, nullable=True)

    category_id: Mapped[int] = Column(Integer, ForeignKey('category.id'), nullable=True)
    category: Mapped[Optional['Category']] = relationship('Category', back_populates='companies', lazy='selectin')

    role_id: Mapped[int] = Column(Integer, ForeignKey('role.id'), nullable=True)
    role: Mapped[Optional['Role']] = relationship('Role', back_populates='companies', lazy='selectin')

    practices: Mapped[Optional['Practice']] = relationship('Practice', back_populates='company',
                                                           lazy='selectin')

    registered_at: Mapped[datetime] = Column(TIMESTAMP, default=datetime.utcnow)
    hashed_password: str = Column(String(length=1024), nullable=False)

    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)

    def __str__(self):
        return self.name


class Student(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'student'

    id: Mapped[int] = Column(Integer, primary_key=True)
    email: Mapped[str] = Column(String, unique=True, nullable=False)
    lastname: Mapped[str] = Column(String, nullable=False)
    firstname: Mapped[str] = Column(String, nullable=False)
    surname: Mapped[str] = Column(String, nullable=False)

    registered_at: Mapped[datetime] = Column(TIMESTAMP, default=datetime.utcnow)

    role_id: Mapped[int] = Column(Integer, ForeignKey('role.id'), nullable=True)
    role: Mapped[Optional['Role']] = relationship('Role', back_populates='students', lazy='selectin')

    provider_id: Mapped[int] = Column(Integer, ForeignKey('provider.id'), nullable=True)
    provider: Mapped[Optional['Provider']] = relationship('Provider', back_populates='students',
                                                          lazy='selectin')

    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
