from fastapi import APIRouter, HTTPException

from ..model.item import Item

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

item = Item(name="gun", price=100000, description="Portal Gun", tax=1.0, tags=["weapon"])


@router.get("/")
async def read_items():
    return item


@router.get("/{item_name}")
async def read_item(item_name: str) -> Item:
    if item_name != item.name:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
