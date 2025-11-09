from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from ..core.database import Base
from sqlalchemy.orm import relationship


class User(Base):
    """User SQLAlchemy model."""
    
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    items = relationship("Item", back_populates="user", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"
