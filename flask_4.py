from flask import Flask # This step will import some variables, such as __name__
#app = Flask("db") # Because db is a real package, so the root path ,static path variables of app object will change to "db" 's directory
#app = Flask("db1") # Because db1 does not exist, so app's variable wouldn't change
#app = Flask("fake_module") # Same as db1 even though fake_module is a real python module, but just a single file
app = Flask(__name__)
print(app.name)