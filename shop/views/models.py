from flask import Blueprint, render_template

routes = Blueprint('models', __name__)


@routes.get('/models')
def get_all():
    return render_template('models.html', content="Models List")
