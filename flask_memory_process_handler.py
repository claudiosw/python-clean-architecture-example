""" Flask In-Memory Process Handler
"""


from src.app.flask_memory.create_flask_memory_app \
    import create_flask_memory_app
from src.infra.loggers.logger_default import LoggerDefault


logger = LoggerDefault()


if __name__ == "__main__":
    flask_memory_app = create_flask_memory_app(logger)
    flask_memory_app.run(debug=True)
