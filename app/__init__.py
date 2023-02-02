from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect()


@app.route('/')
def index():
    return render_template('index.html')


def not_found(error):
    return render_template('error_templates/404.html'), 404


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    print(request.method)
    print(request.form('username'))
    print(request.form('password'))
    """
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == '12345':
            return redirect(url_for('index'))
        else:
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


def app_init(config):
    app.config.from_object(config)
    csrf.init_app(app)
    app.register_error_handler(404, not_found)
    return app