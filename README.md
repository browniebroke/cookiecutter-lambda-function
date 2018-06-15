Cookiecutter Lambda Function
============================

[![CircleCI](https://img.shields.io/circleci/project/github/browniebroke/cookiecutter-lambda-function.svg)](https://circleci.com/gh/browniebroke/cookiecutter-lambda-function)

A cookiecutter template to create AWS Lambda function

Requirements
------------

Install `cookiecutter` command line: `pip install cookiecutter` or `brew install cookiecutter` using Homebrew

Usage
-----

Generate a new Lambda function: `cookiecutter gh:browniebroke/cookiecutter-lambda-function` 

The generated projects uses [Chalice](http://chalice.readthedocs.io/en/latest/) to deploy to AWS
lambda. It uses a Flask-like API to declare the entry points of your serverless infrastructure.

Your serverless application should declare its dependencies in the generated `requirements.txt`.

Options
-------

- `endpoint`: Create a HTTP endpoint entry point - `@app.route` style
- `schedule`: Create a [schedule event](http://chalice.readthedocs.io/en/latest/topics/events.html#scheduled-events)
- `timeout`: Lambda function timeout (default to 60)

Vendoring a dependency
----------------------

If your application depends on a 3rd party which Chalice cannot install on Lambda,
they recommend [vendoring the 3rd party](http://chalice.readthedocs.io/en/latest/topics/packaging.html#rd-party-packages)
dependency in your repository.

The generated project provides a simple command line utility to assist in doing so: `bin/vendor_package.py`.
To use it, make sure the 3rd party is installed in your current python interpreter
(e.g. [PyYAML](https://pypi.org/project/PyYAML/))
 
```bash
pip install PyYAML
```
 
And then pass the python module name as argument to the script, that is the name you use to 
import your 3rd party dependency from your code. PyYAML being imported with `import yaml`,
you vendor it with:

```bash
./bin/vendor_package.py yaml 
```

You can pass as much arguments as you want to the script, they will be copied from your current 
Python interpreter to the vendor directory.

License
-------

This project is licensed under the terms of the [MIT License](/LICENSE)
