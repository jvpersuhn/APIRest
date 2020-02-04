from flask import Flask
from flask_restful import Api

from controller.Administrador_controller import AdministradorController
from controller.Cliente_controller import ClienteController
from controller.Produto_controller import ProdutoController

app = Flask(__name__)
api = Api(app)

api.add_resource(AdministradorController, "/api/Administrador", endpoint="pessoas")
api.add_resource(AdministradorController, "/api/Administrador/<int:id>", endpoint="pessoa")

api.add_resource(ClienteController, "/api/Cliente", endpoint="clientes")
api.add_resource(ClienteController, "/api/Cliente/<int:id>", endpoint="cliente")

api.add_resource(ProdutoController, "/api/Produto", endpoint="produtos")
api.add_resource(ProdutoController, "/api/Produto/<int:id>", endpoint="produto")

app.run(debug=True)