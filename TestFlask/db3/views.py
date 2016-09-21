from db3 import app


@app.route('/')
@app.route('/index')
def index():
    return "db3"