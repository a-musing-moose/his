from typing import List
from uuid import UUID

from .contracts import ListItemRepositoryContract
from .domain import ListItem
from .exceptions import ListItemNotFoundError


class MemoryListItemRepository(ListItemRepositoryContract):

    def __init__(self):
        self.items = {}

    async def create(self, item: ListItem) -> ListItem:
        self.items[item.uuid] = item
        return self.items[item.uuid]

    async def retrieve(self, uuid: UUID) -> ListItem:
        if uuid not in self.items:
            raise ListItemNotFoundError()
        return self.items[uuid]

    async def update(self, item: ListItem) -> ListItem:
        if item.uuid not in self.items:
            raise ListItemNotFoundError()
        self.items[item.uuid] = item
        return item

    async def delete(self, uuid: UUID) -> bool:
        if uuid not in self.items:
            del self.items[uuid]
            return True
        return False

    async def list(self) -> List[ListItem]:
        return list(self.items.values())

    async def empty(self) -> None:
        self.items = {}
