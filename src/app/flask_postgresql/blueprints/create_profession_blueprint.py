""" Flask Blueprint Create Profession
"""


from flask import jsonify
from flask import Blueprint, request, current_app
from src.app.flask_postgresql.controllers.create_profession_controller import \
    CreateProfessionController


blueprint_create_profession = Blueprint('create_profession', __name__)


@blueprint_create_profession.route('/profession/', methods=["POST"])
def create_profession_blueprint():
    """ Create Profession Blueprint
    """
    logger = current_app.config['logger']
    input_json = request.get_json(force=True)
    controller = CreateProfessionController(logger)
    controller.get_profession_info(input_json)
    result = controller.execute()
    return jsonify(result), 201
