from flask import Blueprint, redirect, render_template, request, url_for

from shop.api.client import client

routes = Blueprint('models', __name__)


@routes.get('/')
def get_all():
    models = client.models.get_all()
    return render_template('models.html', page_tittle='models_list', models=models)


@routes.post('/delete')
def delete():
    uid = request.form['uid']
    client.models.delete(uid)
    return redirect(url_for('models.get_all'))
