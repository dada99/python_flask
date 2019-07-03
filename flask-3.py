from flask import Flask, url_for,render_template,Markup
app = Flask(__name__)
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/templetest')    
def templetest():
    return  render_template('templetest.html')
    
if __name__ == '__main__':
    app.run(debug=True)    