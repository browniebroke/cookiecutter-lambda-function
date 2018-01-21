from {{cookiecutter.project_slug}} import app{% if cookiecutter.endpoint == "y" %}


def test_endpoint():
    assert app.index() == {'hello': 'world'}{% endif %}{% if cookiecutter.schedule == "y" %}


def test_schedule():
    assert app.every_hour({'what': 'hello'}) is None{% endif %}
