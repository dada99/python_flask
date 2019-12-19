from flask import Flask# This step will import some variables, such as __name__
#app = Flask("db") # Because db is a real package, so the root path ,static path variables of app object will change to "db" 's directory
#app = Flask("db1") # Because db1 does not exist, so app's variable wouldn't change
#app = Flask("fake_module") # Same as db1 even though fake_module is a real python module, but just a single file
app = Flask(__name__)
print(app.name)

def index():
    return 'This is the index'
app.add_url_rule("/",'',index)
#app.add_url_rule("/",view_func=index) # Same Ok

@app.route("/index")
def index1():
    return 'This is the index1'

if __name__ == '__main__':
    app.run(debug=True)     