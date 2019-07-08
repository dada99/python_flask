from flask import Flask, url_for,render_template,Markup
app = Flask(__name__)

@app.route('/vuepage')    
def vuepage():
    return  render_template('vue.html')
    
if __name__ == '__main__':
    app.run(debug=True)    