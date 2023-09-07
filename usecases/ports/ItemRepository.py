from abc import ABC, abstractmethod

from domain.Item import Item


class ItemRepository(ABC):
    @abstractmethod
    def get_items(self, audience: str, category: str) -> list[Item]:
        pass
