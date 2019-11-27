from flask_restful import Resource, reqparse
from models.reserva import ReservaModel

from flask_jwt import jwt_required

class ReservaController(Resource):
    # @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'fecha_inicio',
            type=str,
            required=True,
            help='Falta la fecha inicio'
        )
        parser.add_argument(
            'fecha_fin',
            type=str,
            required=True,
            help='Falta la fecha fin'
        )
        parser.add_argument(
            'monto',
            type=float,
            required=True,
            help='Falta el monto'
        )
        parser.add_argument(
            'adelanto',
            type=float,
            required=True,
            help='Falta el adelanto'
        )
        parser.add_argument(
            'id_usu',
            type=int,
            required=True,
            help='Falta el id usuario'
        )
        parser.add_argument(
            'id_precio',
            type=int,
            required=True,
            help='Falta el id precio'
        )
        data = parser.parse_args()
        validar = ReservaModel.query.filter_by(pc_id=data['id_precio']).all()
        from datetime import  datetime
        fechaintroducidainicio = datetime.strptime(data['fecha_inicio'],'%Y-%m-%d %H:%M')
        fechaintroducidafin = datetime.strptime(data['fecha_fin'],'%Y-%m-%d %H:%M')
        print(fechaintroducidainicio)
        for sentencia in validar:
            fechaencontradainicio = sentencia.res_fechin
            fechaencontradafin = sentencia.res_fechfin
            print(fechaencontradainicio)
            print(fechaencontradafin)
            if(fechaintroducidainicio>=fechaencontradainicio and fechaintroducidainicio <fechaencontradafin) or (fechaintroducidafin>fechaencontradainicio and fechaintroducidafin<=fechaencontradafin) or (fechaintroducidainicio==fechaencontradainicio and fechaintroducidafin==fechaencontradafin) or (fechaintroducidainicio<fechaencontradainicio and fechaintroducidafin>fechaencontradafin):
                return {'message':'Ya hay una reserva'}
                # print(fechaencontradainicio)
        return 'ok'
        insercion = ReservaModel(data['fecha_inicio'],data['fecha_fin'],data['monto'],data['adelanto'],data['id_usu'],data['id_precio'])
        try:
            insercion.guardar_en_la_bd()
        except:
            return {
                'message':'Hubo un error al guardar la reserva, intentelo nuevamente'
                },500
        return {
            'message':'Reserva creada satisfactoriamente',
            'content':insercion.res_id
        },201