Cookiecutter Lambda Function
============================

A cookiecutter template to create AWS Lambda function

Requirements
------------

Install `cookiecutter` command line: `pip install cookiecutter` or `brew install cookiecutter` using Homebrew

Usage
-----

Generate a new Lambda function: `cookiecutter gh:browniebroke/cookiecutter-lambda-function` 

The generated projects uses [Chalice](http://chalice.readthedocs.io/en/latest/) to deploy to AWS
lambda. It uses a Flask-like API to declare the entry points of your serverless infrastructure.

It's recommended to install this in a virtualenv, and the modern way to do it
is to use [pipenv](https://docs.pipenv.org/) for that.

Your serverless application should declare its dependencies in the generated `requirements.txt`.

Options
-------

- `endpoint`: Create a HTTP endpoint entry point - `@app.route` style
- `schedule`: Create a [schedule event](http://chalice.readthedocs.io/en/latest/topics/events.html#scheduled-events)

License
-------

This project is licensed under the terms of the [MIT License](/LICENSE)
