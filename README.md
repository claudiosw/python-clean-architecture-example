![tests](https://github.com/claudiosw/python-clean-architecture-example/workflows/pytesting/badge.svg) &nbsp; ![code coverage](https://raw.githubusercontent.com/claudiosw/python-clean-architecture-example/coverage-badge/coverage.svg?raw=true)

# About
This repository is a simple example of an implementation Clean Architecture using Python.

# Articles about this project
I am writing a series of Linkedin articles related to this project:
* [Python Clean Architecture In-memory CLI implementation](https://www.linkedin.com/pulse/implementation-clean-architecture-python-part-1-cli-watanabe/): I wrote [this article](https://www.linkedin.com/pulse/implementation-clean-architecture-python-part-1-cli-watanabe/) explaining the Clean Architecture, its layers and a Python implementation of an in-memory CLI.
* [Error Handling, Logging and Validation implementation in Python Clean Architecture](https://www.linkedin.com/pulse/implementation-clean-architecture-python-part-2-error-watanabe/): I wrote [this article](https://www.linkedin.com/pulse/implementation-clean-architecture-python-part-2-error-watanabe/) about error handling, logging and validation, including some Python best practices around these topics. I complemented our Python Clean Architecture implementation with those topics.

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