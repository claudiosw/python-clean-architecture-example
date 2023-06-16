""" Main Flask PostgreSQL app
"""


from flask import Flask, g
from werkzeug.exceptions import HTTPException
from src.app.flask_postgresql.blueprints.create_profession_blueprint \
    import blueprint_create_profession
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.interactor.errors.error_classes \
    import FieldValueNotPermittedException
from src.infra.db_models.db_base import Session
from src.interactor.errors.error_classes import UniqueViolationError


def format_error_response(
        error: Exception,
        error_code: int,
        logger: LoggerInterface
):
    """ Format Error Response """
    logger.log_exception(f"500 - Internal Server Error: {str(error)}")

    response = {
        'status_code': error_code,
        'error': error.__class__.__name__,
        'message': str(error)
    }
    return response, error_code


def create_flask_postgresql_app(logger: LoggerInterface):
    """ Create Main Flask PostgreSQL app
    """
    app = Flask(__name__)
    app.config['logger'] = logger
    app.register_blueprint(blueprint_create_profession, url_prefix='/v1')

    @app.errorhandler(HTTPException)
    def handle_http_error(error: HTTPException):
        """ Handle HTTP Error Response """
        logger.log_exception(str(error.__class__.__name__))
        logger.log_exception(str(error.description))
        response = {
            'error': error.__class__.__name__,
            'message': error.description,
        }
        return response, error.code

    @app.errorhandler(ValueError)
    def handle_value_error(error: ValueError):
        """ Handle Value Error Response """
        return format_error_response(error, 400, logger)

    @app.errorhandler(FieldValueNotPermittedException)
    def handle_field_not_permitted_error(
        error: FieldValueNotPermittedException
    ):
        """ Handle Value Error Response """
        return format_error_response(error, 400, logger)

    @app.errorhandler(UniqueViolationError)
    def handle_unique_violation_error(error: UniqueViolationError):
        """ Handle Unique Violation Error Response """
        return format_error_response(error, 409, logger)

    @app.errorhandler(Exception)
    def handle_general_exception(error):
        """ Handle Other Errors Response """
        return format_error_response(error, 500, logger)

    @app.before_request
    def before_request():
        """ Before Request """
        g.db = Session()

    @app.teardown_request
    def teardown_request(_unused=False):
        """ After Request """
        dbc = getattr(g, 'db', None)
        if dbc is not None:
            dbc.close()

    return app
