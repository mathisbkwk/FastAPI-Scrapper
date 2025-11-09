from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from ..core.database import Base
from sqlalchemy.orm import relationship


class Item(Base):
    """Item SQLAlchemy model."""
    
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    user = relationship("User", back_populates="items")
    
    def __repr__(self):
        return f"<Item(id={self.id}, name='{self.name}')>"
