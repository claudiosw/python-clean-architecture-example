![tests](https://github.com/claudiosw/python-clean-architecture-example/workflows/pytesting/badge.svg) &nbsp; ![code coverage](https://raw.githubusercontent.com/claudiosw/python-clean-architecture-example/coverage-badge/coverage.svg?raw=true)

# About
This repository is a simple example of an implementation Clean Architecture using Python.

# Articles about this project
I am writing a series of Linkedin articles related to this project:
* [Python Clean Architecture In-memory CLI implementation](https://www.linkedin.com/pulse/implementation-clean-architecture-python-part-1-cli-watanabe/): I wrote [this article](https://www.linkedin.com/pulse/implementation-clean-architecture-python-part-1-cli-watanabe/) explaining the Clean Architecture, its layers and a Python implementation of an in-memory CLI.
* [Error Handling, Logging and Validation implementation in Python Clean Architecture](https://www.linkedin.com/pulse/implementation-clean-architecture-python-part-2-error-watanabe/): I wrote [this article](https://www.linkedin.com/pulse/implementation-clean-architecture-python-part-2-error-watanabe/) about error handling, logging and validation, including some Python best practices around these topics. I complemented our Python Clean Architecture implementation with those topics.
* [Python Clean Architecture Flask Web API In-memory implementation](https://www.linkedin.com/pulse/implementation-clean-architecture-python-part-3-adding-watanabe/): In [this article](https://www.linkedin.com/pulse/implementation-clean-architecture-python-part-3-adding-watanabe/), I wrote about basic Flask concepts, Flask blueprints and how to test a Flask application. I also talked about the addition of a Flask web API to our Python Clean Architecture implementation. 
* [Python Clean Architecture Flask Web API Postgresql implementation](https//www.linkedin.com/pulse/implementation-clean-architecture-python-part-4-adding-watanabe/): In [this article](https//www.linkedin.com/pulse/implementation-clean-architecture-python-part-4-adding-watanabe/), I wrote about about the inclusion of the Flask PostgreSQL flavour in my Python Clean Architecture repository. I talked about the SQLAlchemy model, Alembic database migrations, using .env files to protect sensitive information and also how to close the database connection when the http connection is closed.

Also, [check this repository](https://github.com/claudiosw/python-best-practices) where you can find examples and explanations of Python best practices that complement this repository and its articles.

# Instalation

## On prompt, acess the directory that want to download the project
```
git clone https://github.com/claudiosw/python-clean-architecture-example-1.git
```

## Create the virtual environment:
```
python -m venv venv

```

## Run the virtual environment:
### Windows
```
venv\Scripts\activate

```
### Linux/MacOS
```
source venv/bin/activate
```

## Install the required Python packages:
```
pip install -r requirements.txt
pre-commit install
```

# Run the In-Memory CLI
```
python .\cli_memory_process_handler.py
```

# Run the In-Memory Flask API
```
python .\flask_memory_process_handler.py
```

# Prepare the PostgreSQL database

To use the PostgreSQL flavour of our app, we need to install PostgreSQL software. It can be in other machine as well. We will need a database and a user to access this database.

Create a .env file. Use the .env.example file as a template. Set the values considering your scenario.

## Apply database migrations

With the PostgreSQL database installed and configured, you can apply the database migrations with the command below:

```
alembic upgrade head
```

# Run the PostgreSQL Flask API
```
python .\flask_postgresql_process_handler.py
```

# Documentation

## API Documentation of the Flask PostgreSQL flavor of this project:
You can access the API documentation [here](https://documenter.getpostman.com/view/27866946/2s93saZYEK).


# Closing

I hope this repository and my article series were valuable to you. If that was the case, please star it.

If you want to contact me, reach me on [LinkedIn](https://www.linkedin.com/in/claudiosw/) or [Twitter](https://twitter.com/ClaudioShigueoW).

I am looking for a Python position. I also offer paid mentoring.