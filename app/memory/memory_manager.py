from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.memory.database import Base, engine, SessionLocal


class Memory(Base):
    __tablename__ = "memories"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, nullable=False)
    content = Column(String, nullable=False)
    importance = Column(Integer, default=3)
    created_at = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(bind=engine)


class MemoryManager:

    def add_memory(self, category, content, importance=3):
        db = SessionLocal()

        memory = Memory(
            category=category,
            content=content,
            importance=importance
        )

        db.add(memory)
        db.commit()
        db.refresh(memory)
        db.close()

        return memory

    def get_memories(self):
        db = SessionLocal()

        memories = (
            db.query(Memory)
            .order_by(Memory.importance.desc())
            .all()
        )

        db.close()

        return memories

    def search_memory(self, keyword):
        db = SessionLocal()

        memories = (
            db.query(Memory)
            .filter(Memory.content.contains(keyword))
            .all()
        )

        db.close()

        return memories

    def delete_memory(self, memory_id):
        db = SessionLocal()

        memory = db.query(Memory).filter(Memory.id == memory_id).first()

        if memory:
            db.delete(memory)
            db.commit()

        db.close()