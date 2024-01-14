from flask import Flask, jsonify
import random
from webapp_api_server.webapp_components.test_comp1 import square_of

from webapp_api_server.api_services.srv1.srv1_ctrl1 import bp as srv1_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(srv1_bp)

    @app.route('/init')
    def init_page():
        return jsonify({
            "message": "let's begin",
            "val": square_of(random.randint(100, 1000))
        })
    return app