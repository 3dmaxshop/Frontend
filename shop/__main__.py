from flask import Flask, render_template

from shop.config import config
from shop.views import models

app = Flask(__name__)

app.register_blueprint(models.routes, url_prefix='/')


@app.route('/')
def index():
    name_project = '3dMaxShop'
    return render_template('index.html', content='3dshop')


if __name__ == '__main__':
    app.run(host=config.server.host, port=config.server.port)
