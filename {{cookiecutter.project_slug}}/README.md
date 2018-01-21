{{ cookiecutter.project_name }}
==============================

{{ cookiecutter.project_short_description }}

Requirements
------------

This project uses [pipenv](https://docs.pipenv.org/) to manage its dependencies, it can be installed
on macOS using [Homebrew](https://brew.sh) by typing `$ brew install pipenv`.

Installation
------------

This project uses [Chalice](http://chalice.readthedocs.io/en/latest/) to deploy to AWS
lambda. Chalice provides a Flask-like API to declare the entry points of your serverless 
infrastructure. Chalice is installed in an isolated environment by running:

    ```
    pipenv install
    ```
    
Testing
-------

Uses pytest. To run the whole test suite:

    ```
    pipenv run pytest
    ```

Deployment
----------

See [Chalice documentation](http://chalice.readthedocs.io/en/latest/quickstart.html#credentials),
you will need to have your AWS credentials setup, and then you can run Chalice inside of your
virtualenv:

    ```
    pipenv run chalice deploy
    ```

Credits
-------

This project has been generated with [Cookiecutter](https://github.com/audreyr/cookiecutter)
using the [Lambda function template](https://github.com/browniebroke/cookiecutter-lambda-function)
