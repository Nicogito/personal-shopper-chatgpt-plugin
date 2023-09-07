import json

from flask import request, Response

from infrastructure.web.controllers.GetItemsBodyRequest import GetItemsBodyRequest
from usecases.GetItems import GetItems


class Controller():
    def __init__(self, get_items: GetItems):
        self.get_items = get_items

    def execute(self):
        try:
            get_items_body_request = GetItemsBodyRequest(request.args.get('audience'), request.args.get('category'))
        except AttributeError:
            return Response('{"message": "Invalid request"}', status=400, mimetype='application/json')
        if not get_items_body_request.validate():
            return Response('{"message": "Invalid body request"}', status=400, mimetype='application/json')
        items = self.get_items.execute(get_items_body_request.audience, get_items_body_request.category)
        return Response(json.dumps([i.__dict__ for i in items]), status=200, mimetype='application/json')

