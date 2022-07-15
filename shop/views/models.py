from typing import Any

from flask import Blueprint, redirect, render_template, request, url_for

from shop.api.client import client
from shop.api.schemas import Model
from shop.api.schemas import Category

routes = Blueprint('models', __name__)


def filter_category(models, category_id):

    return [model for model in models if model.category_id == category_id]


@routes.get('/')
def get_all():
    models = client.models.get_all()
    categories = client.categories.get_all()
    selected_category = request.args.get('category_id')
    if selected_category:
        models = filter_category(models, selected_category)

    return render_template('models.html', page_tittle='models_list', models=models, categories=categories)


@routes.post('/delete')
def delete():
    uid = request.form['uid']
    client.models.delete(uid)
    return redirect(url_for('models.get_all'))


@routes.post('/change')
def change():
    payload: dict[str, Any] = dict(request.form)
    payload = Model(**payload)
    client.models.change(payload)
    return redirect(url_for('models.get_all'))


@routes.post('/add')
def add():
    payload: dict[str, Any] = dict(request.form)
    payload['uid'] = 1
    model = Model(**payload)
    client.models.add(model)
    return redirect(url_for('models.get_all'))


@routes.get('/edit/<int:uid>')
def edit_page(uid):
    model = client.models.get_by_uid(uid)
    categories = client.categories.get_all()
    return render_template('model_edit.html', model=model, categories=categories)


@routes.post('/search')
def search_category():
    payload = dict(request.form)

    return redirect(url_for(
        'models.get_all',
        category_id=payload.get('category_id'),
    ))
