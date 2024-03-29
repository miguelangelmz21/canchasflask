from flask_restful import Resource, reqparse

from models.precioCancha import PrecioCanchaModel

class PrecioCanchaController(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'descripcion',
            type=str,
            required=True,
            help='Falta el descripcion'
        )
        parser.add_argument(
            'monto',
            type=float,
            required=True,
            help='Falta el monto'
        )
        parser.add_argument(
            'disponible',
            type=bool,
            required=True,
            help='Falta el disponibilidad'
        )
        parser.add_argument(
            'cancha_id',
            type=int,
            required=True,
            help='Falta el id cancha'
        )
        data = parser.parse_args()
        insercion = PrecioCanchaModel(data['descripcion'],data['monto'],data['disponible'],data['cancha_id'])
        try:
            insercion.guardar_en_la_bd()
        except:
            return {
                'message':'Hubo un error al agregar un precio a la cancha, intente nuevamente'
            },500
        return { 
            'message':'Se agrego exitosamente el precio a la cancha'+str(insercion.can_id)
        },201
    def get(self,id):
        resultado = PrecioCanchaModel.query.filter_by(can_id=id).filter_by(pc_disponibilidad=True).first()
        if resultado:
            return resultado.retornar_json()
        return {'message':'Esa cancha aun no tiene precios disponible'},200

    def put(self,id):
        parser = reqparse.RequestParser()
        parser.add_argument('estado',
            type=bool,
            required = True,
            help = 'Falta el estado que va a ser cambiado el precio de la cancha')
        data = parser.parse_args()
        resultado = PrecioCanchaModel.query.filter_by(pc_id=id).first()
        try:
            resultado.actualizar_estado(data['estado'])
        except:
            return {
                'message':'Hubo un error al actualizar el estado, intentelo nuevamente'
            },500
        return {
            'message':'Se actualizo el estado del precio de esa canchita'
        },200
