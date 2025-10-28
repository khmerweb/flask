
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List, Optional
from .database import engine


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "User"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] = mapped_column(nullable=False)
    thumb: Mapped[str] = mapped_column()
    content: Mapped[str] = mapped_column()
    date: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return f"User(id={self.id!r})"
    

Base.metadata.create_all(engine, checkfirst=True)