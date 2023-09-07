from infrastructure.dataproviders.GraphItemRepository import GraphItemRepository
from infrastructure.web.controllers.Controller import Controller
from infrastructure.web.Router import Router
from usecases.GetItems import GetItems


def run():
    item_repository = GraphItemRepository()
    get_items = GetItems(item_repository)
    web_controller = Controller(get_items)
    Router.run(web_controller)


if __name__ == '__main__':
    run()
