from flask import Flask,render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

def index():
    return 'This is the index'
app.add_url_rule("/",'',index)
#app.add_url_rule("/",view_func=index) # Same Ok

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)     