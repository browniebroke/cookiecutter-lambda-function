from chalice import Chalice

app = Chalice(app_name='{{ cookiecutter.project_slug }}')
{%- if cookiecutter.endpoint == "y" %}


@app.route('/')
def index():
    return {'hello': 'world'}
{%- endif %}
{%- if cookiecutter.schedule == "y" %}


@app.schedule('rate(1 hour)')
def every_hour(event):
    print(event.to_dict())
{%- endif %}
