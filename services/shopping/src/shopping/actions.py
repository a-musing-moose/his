from typing import List
from uuid import UUID

from almanac import services

from .contracts import ListItemRepositoryContract
from .domain import ListItem
from .types import UUIDType

__all__ = [
    'add_item',
    'list_items',
    'fetch_item',
    'update_item_description',
    'check_item',
    'uncheck_item',
    'delete_item',
    'clear_list'
]


def _ensure_UUID(uuid: UUIDType) -> UUID:
    if not isinstance(uuid, UUID):
        uuid = UUID(uuid)
    return uuid


def _item_repo() -> ListItemRepositoryContract:
    return services.get(ListItemRepositoryContract)


async def add_item(description: str) -> ListItem:
    item = ListItem({'description': description})
    item.validate()
    return await _item_repo().create(item)


async def list_items() -> List[ListItem]:
    return await _item_repo().list()


async def fetch_item(uuid: UUIDType) -> ListItem:
    uuid = _ensure_UUID(uuid)
    return await _item_repo().retrieve(uuid)


async def update_item_description(uuid: UUIDType, description: str) -> ListItem:
    item = await fetch_item(uuid)
    item.description = description
    return await _item_repo().update(item)


async def check_item(uuid: UUIDType) -> ListItem:
    item = await fetch_item(uuid)
    item.checked = True
    return await _item_repo().update(item)


async def uncheck_item(uuid: UUIDType) -> ListItem:
    item = await fetch_item(uuid)
    item.checked = False
    return await _item_repo().update(item)


async def delete_item(uuid: UUIDType) -> bool:
    uuid = _ensure_UUID(uuid)
    return await _item_repo().delete(uuid)


async def clear_list() -> None:
    await _item_repo().empty()
