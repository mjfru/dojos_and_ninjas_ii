from flask_app.controllers import dojos  ## Name of the controller files, no .py
from flask_app import app

if __name__ == "__main__":
    app.run(debug = True)
