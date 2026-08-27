from datetime import datetime, timezone
from typing import List

from fastapi import APIRouter, HTTPException, status

from app.core.config import settings
from app.models.schemas import (
    HealthResponse,
    Item,
    ItemCreate,
    ItemUpdate,
    MessageResponse,
)

router = APIRouter()

# In-memory store (replace with a real database later)
_items: dict[int, Item] = {}
_next_id = 1


@router.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check() -> HealthResponse:
    """Check API health status."""
    return HealthResponse(
        status="ok",
        timestamp=datetime.now(timezone.utc),
        version=settings.app_version,
    )


@router.get("/items", response_model=List[Item], tags=["Items"])
async def list_items() -> List[Item]:
    """Return all items."""
    return list(_items.values())


@router.post(
    "/items",
    response_model=Item,
    status_code=status.HTTP_201_CREATED,
    tags=["Items"],
)
async def create_item(item_in: ItemCreate) -> Item:
    """Create a new item."""
    global _next_id
    item = Item(
        id=_next_id,
        name=item_in.name,
        description=item_in.description,
        price=item_in.price,
        created_at=datetime.now(timezone.utc),
    )
    _items[_next_id] = item
    _next_id += 1
    return item


@router.get("/items/{item_id}", response_model=Item, tags=["Items"])
async def get_item(item_id: int) -> Item:
    """Get a single item by ID."""
    item = _items.get(item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )
    return item


@router.put("/items/{item_id}", response_model=Item, tags=["Items"])
async def update_item(item_id: int, item_in: ItemUpdate) -> Item:
    """Update an existing item."""
    item = _items.get(item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )

    update_data = item_in.model_dump(exclude_unset=True)
    updated = item.model_copy(update=update_data)
    _items[item_id] = updated
    return updated


@router.delete(
    "/items/{item_id}",
    response_model=MessageResponse,
    tags=["Items"],
)
async def delete_item(item_id: int) -> MessageResponse:
    """Delete an item."""
    if item_id not in _items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )
    del _items[item_id]
    return MessageResponse(message=f"Item {item_id} deleted successfully")
