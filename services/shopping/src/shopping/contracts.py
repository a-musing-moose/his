import abc
from typing import List
from uuid import UUID

from .domain import ListItem


class ListItemRepositoryContract(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    async def create(self, item: ListItem) -> ListItem:
        ...

    @abc.abstractmethod
    async def retrieve(self, uuid: UUID) -> ListItem:
        ...

    @abc.abstractmethod
    async def update(self, item: ListItem) -> ListItem:
        ...

    @abc.abstractmethod
    async def delete(self, uuid: UUID) -> bool:
        ...

    @abc.abstractmethod
    async def list(self) -> List[ListItem]:
        ...

    @abc.abstractmethod
    async def empty(self) -> None:
        ...
