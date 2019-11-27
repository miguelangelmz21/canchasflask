from flask import Flask
from flask_restful import Api

from base_de_Datos import bd
# from models.local import LocalModel
from controllers.local import LocalController, LocalesController
# from models.canchita import CanchitaModel
from controllers.canchita import CanchitaController, CanchitasController
# from models.tipo import TipoModel
from controllers.tipo import TipoController
# from models.usuario import UsuarioModel
from controllers.usuario import UsuarioController
# from models.localOpcionesLocal import LocalOpcionesLocalModel
from controllers.localOpcionesLocal import LocalOpcionesLocalController
# from models.opcionesLocal import opcionesLocalModel
from controllers.opcionesLocal import OpcionesLocalController, OpcionesLocalTodosController
from controllers.precioCancha import PrecioCanchaController
from models.precioCancha import PrecioCanchaModel
# from models.reserva import ReservaModel
from controllers.reserva import ReservaController
from models.valoraciones import ValoracionesModel
from controllers.valoraciones import ValoracionController,ValoracionesController

# Librerias para el JWT
from flask_jwt import JWT
from seguridad import autentication, identificador
 
 from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:root@localhost/canchas"
app.config['SQLALCHEMY_DATABASE_URI']="mysql://z3YWkuyTTF:AQZDC7JED7@remotemysql.com/z3YWkuyTTF"
app.config['SECRET_KEY'] = 'clave_secreta'
app.config['JWT_AUTH_URL_RULE']='/usuario/login'
import datetime
# app.config['JWT_EXPIRATION_DELTA']=datetime.timedelta(days=5,hour=12)
app.config['JWT_EXPIRATION_DELTA']=datetime.timedelta(hours=1)
#OJO la linea de arriba SIEMPRE antes de la siguiente linea
jsonwebtoken = JWT(app, autentication, identificador)
api = Api(app)

#miguel@gmail.com
#123456
@app.route('/')
def inicio():
    return 'La API REST ha escuchado tu peticion'

@app.before_first_request
def iniciar_bd():
    #Para iniciar la aplicacion de SQL ALCHEMY
    bd.init_app(app)
    # bd.drop_all(app=app)
    #Para crear todas las tablas
    bd.create_all(app=app)


api.add_resource(TipoController,'/tipo/buscar/<string:nombre>','/tipo/crear')
api.add_resource(CanchitaController,'/cancha/buscar/<int:id>','/cancha/crear')
api.add_resource(LocalController,'/local/crear','/local/buscar/<string:nombre>')
api.add_resource(CanchitasController,'/canchas/traertodos')
api.add_resource(OpcionesLocalController,'/opciones/agregar','/opciones/buscar/<string:nombre>')
api.add_resource(PrecioCanchaController,'/preciocancha/crear','/preciocancha/buscar/<int:id>','/preciocancha/actualizar/<int:id>')
api.add_resource(OpcionesLocalTodosController,'/opciones/traertodos')
api.add_resource(LocalesController,'/local/traertodos')
api.add_resource(LocalOpcionesLocalController,'/localopciones/agregar')
api.add_resource(ReservaController, '/reserva/crear')
api.add_resource(UsuarioController,'/usuario/crear')
api.add_resource(ValoracionesController,'/valoraciones/local/<int:id_local>')
if(__name__=="__main__"):
    app.run(debug=True)