from flask import Flask
from flask_scss import Scss
from flask_assets import Environment, Bundle


def create_app():
    app = Flask(__name__)
    app.config["JSON_AS_ASCII"] = False

    # scssの設定
    Scss(app, static_dir='web/static/css', asset_dir='assets/scss')

    # jsのbundle
    assets = Environment(app)
    js = Bundle('../../assets/js/table.js', '../../assets/js/main.js', output='./js/script.js', filters='jsmin')
    assets.register('js_all', js)

    return app

app = create_app()
from . import route
