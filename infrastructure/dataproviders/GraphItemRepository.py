from neo4j import GraphDatabase

from domain.Item import Item
from usecases.ports.ItemRepository import ItemRepository


class GraphItemRepository(ItemRepository):

    def __init__(self):
        self.driver = GraphDatabase.driver("bolt://localhost:7687",
                                           auth=("neo4j", "toto"))

    def close(self):
        self.driver.close()

    def get_items(self, audience: str, category: str) -> list[Item]:
        def get_items_transaction(tx, audience: str, category: str):
            cypher_query = """
                        MATCH (:Audience {name:$audience})<-[:IS_DESTINED_TO]-(i:Item)-[:IS_A]->(t:Type{name:$category})
                        RETURN i
                    """

            result = tx.run(cypher_query, audience=audience, category=category)
            return [row.data()['i'] for row in result]

        items = []
        with self.driver.session() as session:
            query_result = session.execute_read(get_items_transaction, audience, category)
        for item in query_result:
            items.append(Item(item["name"], item["price"], item["url"]))
        return items
