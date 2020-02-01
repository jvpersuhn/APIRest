from flask import Flask
from flask_restful import Api

from controller.Administrador_controller import AdministradorController

app = Flask(__name__)
api = Api(app)

api.add_resource(AdministradorController, "/api/Administrador", endpoint="pessoas")
api.add_resource(AdministradorController, "/api/Administrador/<int:id>", endpoint="pessoa")

app.run(debug=True)