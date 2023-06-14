""" Flask PostgreSQL Process Handler
"""


from src.app.flask_postgresql.create_flask_postgresql_app \
    import create_flask_postgresql_app
from src.infra.loggers.logger_default import LoggerDefault


logger = LoggerDefault()


if __name__ == "__main__":
    flask_memory_app = create_flask_postgresql_app(logger)
    flask_memory_app.run(debug=True)
