from flask import Blueprint, redirect, render_template, request, url_for

from shop.api.client import client

from typing import Any

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


@routes.post('/change')
def change():
    payload: dict[str, Any] = dict(request.form)
    client.models.change(payload)
    return redirect(url_for('models.get_all'))
