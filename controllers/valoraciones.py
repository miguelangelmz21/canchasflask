from flask_restful import Resource, reqparse
from models.local import LocalModel
from models.valoraciones import ValoracionesModel

from flask_jwt import jwt_required
class ValoracionController(Resource):
    # @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'comentario',
            type=str,
            required=True,
            help='Falta el comentario'
        )
        parser.add_argument(
            'estrellas',
            type=int,
            required=True,
            help='Falta la cantidad de estrellas'
        )
        parser.add_argument(
            'id_reserva',
            type=int,
            required=True,
            help='Falta el id de reserva'
        )
        data = parser.parse_args()
        valoracion = ValoracionesModel(data['comentario'],data['estrellas'],data['id_reserva'])
        try:
            valoracion.guardar_en_la_bd()
        except:
            return {
                'message':'Hubo un error al ingresar tu comentario, intentalo nuevamente'
            },500
        return {
            'message':'Se agrego exitosamente el comentario',
            'content': valoracion.val_id
        },201

class ValoracionesController(Resource):
    def get(self,id_local):
        #hacer que me traiga todas las valoraciones del local
        sentencia = LocalModel.query.filter_by(loc_id=id_local).first()
        resultado = []
        promedio = 0
        # print(sentencia.canchitas[0].preciocancha[0].reservas[0].valoraciones)
        for cancha in sentencia.canchitas:
            print(cancha)
            for preciocancha in cancha.preciocancha:
                for reserva in preciocancha.reservas:
                    for valoracion in reserva.valoraciones:
                        promedio += valoracion.val_estrellas
                        resultado.append({'comentario':valoracion.val_comentario,'estrellas':valoracion.val_estrellas})

        return {
            'comentarios':resultado,
            'promedio':promedio/len(resultado)
        }