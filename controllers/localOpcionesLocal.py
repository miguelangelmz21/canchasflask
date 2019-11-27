from flask_restful import Resource, reqparse

from models.localOpcionesLocal import LocalOpcionesLocalModel

class LocalOpcionesLocalController(Resource):
    # def get(self,nombre):
    #     resultado = LocalModel.query.filter_by(loc_nombre=nombre).all()
    #     if resultado:
    #         resultadoFinal=[]
    #         for item in resultado:
    #             resultadoFinal.append(item.retornar_json())
    #         print(resultado)
    #         return resultadoFinal
    #     return {'message':'No hay ningun local con ese nombre'},404

    def post(self):
        parser =  reqparse.RequestParser()
        parser.add_argument('id_local',
        type=int,
        required=True,
        help='Falta el id del local'
        )
        parser.add_argument('id_opciones',
        type=int,
        required=True,
        help='Falta el id de opciones'
        )
        data = parser.parse_args()
        try:
            LocalOpcionesLocalModel(data['id_local'],data['id_opciones']).guardar_en_la_bd()
        except:
            return {
                'message':'Hubo un error al vincular el local con sus opciones, intente nuevamente'
            },500
        return {
            'message':'Se agrego exitosamente las opciones del local'
        },200

