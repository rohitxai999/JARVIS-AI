from fastapi import APIRouter
from app.memory.memory_manager import MemoryManager

router = APIRouter(
    prefix="/memory",
    tags=["Memory"]
)

memory_manager = MemoryManager()


@router.post("/add")
def add_memory(
    category: str,
    content: str,
    importance: int = 3
):
    memory = memory_manager.add_memory(
        category,
        content,
        importance
    )

    return {
        "message": "Memory added successfully",
        "memory": {
            "id": memory.id,
            "category": memory.category,
            "content": memory.content,
            "importance": memory.importance
        }
    }


@router.get("/")
def get_memories():
    memories = memory_manager.get_memories()

    return [
        {
            "id": memory.id,
            "category": memory.category,
            "content": memory.content,
            "importance": memory.importance
        }
        for memory in memories
    ]


@router.get("/search")
def search_memory(keyword: str):

    memories = memory_manager.search_memory(keyword)

    return [
        {
            "id": memory.id,
            "category": memory.category,
            "content": memory.content,
            "importance": memory.importance
        }
        for memory in memories
    ]


@router.delete("/{memory_id}")
def delete_memory(memory_id: int):

    memory_manager.delete_memory(memory_id)

    return {
        "message": "Memory deleted"
    }