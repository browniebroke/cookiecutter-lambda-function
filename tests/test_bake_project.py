import os
import subprocess
from contextlib import contextmanager

import pytest


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


def test_project_tree(cookies):
    result = cookies.bake(extra_context={'project_slug': 'lambda_func'})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'lambda_func'
    assert result.project.isdir()
    assert result.project.join('app.py').isfile()
    assert result.project.join('requirements.txt').isfile()
    assert result.project.join('requirements-tests.txt').isfile()
    assert result.project.join('.chalice').isdir()
    assert result.project.join('.chalice', 'config.json').isfile()


def test_app_content(cookies):
    result = cookies.bake(extra_context={'project_slug': 'my_handler'})
    app_file = result.project.join('app.py')
    lines = app_file.readlines()
    assert "from chalice import Chalice" in ''.join(lines)
    assert "app = Chalice(app_name='my_handler')" in ''.join(lines)
    assert "@app.route('/')" in ''.join(lines)
    assert "@app.schedule('rate(1 hour)')" in ''.join(lines)


def test_app_content_schedule(cookies):
    result = cookies.bake(extra_context={
        'project_slug': 'my_handler',
        'endpoint': 'n',
    })
    app_file = result.project.join('app.py')
    lines = app_file.readlines()
    assert "@app.schedule('rate(1 hour)')" in ''.join(lines)
    assert "@app.route('/')" not in ''.join(lines)


def test_app_content_endpoint(cookies):
    result = cookies.bake(extra_context={
        'project_slug': 'my_handler',
        'schedule': 'n',
    })
    app_file = result.project.join('app.py')
    lines = app_file.readlines()
    assert "@app.schedule('rate(1 hour)')" not in ''.join(lines)
    assert "@app.route('/')" in ''.join(lines)


flake8_test_data = [
    {},
    {'endpoint': 'n'},
    {'schedule': 'n'},
]


@pytest.mark.parametrize("kwargs", flake8_test_data)
def test_run_flake8(cookies, kwargs):
    result = cookies.bake(extra_context={'project_slug': 'my_handler', **kwargs})
    with inside_dir(str(result.project)):
        assert subprocess.check_call(['flake8']) == 0
