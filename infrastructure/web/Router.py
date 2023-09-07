from flask import Flask

from infrastructure.web.controllers.Controller import Controller


class Router:
    @staticmethod
    def run(web_controller: Controller):
        app = Flask(__name__)

        @app.route('/health')
        def health_check():
            return 'ok'

        @app.route('/items')
        def get_items():
            return web_controller.execute()

        app.run(port=8080, debug=True)
