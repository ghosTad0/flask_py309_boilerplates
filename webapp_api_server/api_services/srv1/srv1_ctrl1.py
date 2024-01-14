from flask import blueprints, jsonify
import random

from webapp_api_server.api_services.srv2.srv2_utils import srv2_number_of_fields

bp = blueprints.Blueprint(name="bp_srv1", import_name="__name__", url_prefix="/srv1")

@bp.route("/init")
def srv1_init():
    srv1_init_data = {
        "message": "srv1 initiated!!",
        "status": "ACTIVE",
        "value": random.randint(1, 100),
        "__name__": __name__
    }
    srv1_init_data['number_of_fields'] = srv2_number_of_fields(srv1_init_data) + 1
    return jsonify(srv1_init_data)
