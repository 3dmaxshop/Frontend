from flask import Blueprint, render_template

from shop.api.client import client

routes = Blueprint('models', __name__)


@routes.get('/')
def get_all():
    models = client.models.get_all()
    return render_template('models.html', page_tittle='models_list', models=models)
