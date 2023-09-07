from domain.Item import Item
from usecases.ports.ItemRepository import ItemRepository


class GetItems:
    def __init__(self, itemRepository: ItemRepository):
        self.itemRepository = itemRepository

    def execute(self, audience: str, category: str) -> list[Item]:
        return self.itemRepository.get_items(audience, category)
