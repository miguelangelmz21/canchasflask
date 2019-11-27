from flask_restful import Resource, reqparse

from models.canchita import CanchitaModel

class CanchitaController(Resource):
    def get(self,id):
        resultado = CanchitaModel.query.filter_by(can_id=id).first()
        print(resultado)
        if resultado:
            return "ok"
        return {
            'message':'No hay ninguna cancha con el id '+str(id)
        },404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'tamanio',
            type=str,
            required=True,
            help='Falta tamanio'
        )
        parser.add_argument(
            'foto',
            type=str,
            required=True,
            help='Falta foto'
        )
        parser.add_argument(
            'local',
            type=int,
            required=True,
            help='Falta local'
        )
        parser.add_argument(
            'tipo',
            type=int,
            required=True,
            help='Falta tipo'
        )
        data = parser.parse_args()
        canchita = CanchitaModel(data['tamanio'],data['foto'],data['local'],data['tipo'])
        try:
            canchita.guardar_en_la_bd()
        except:
            return {'message':'Hubo un error al registrar la canchita, intente nuevamente'},500
        return {'message':'Canchita guardada con exito',
        'contenido':canchita.retornar_json()},201
    
class CanchitasController(Resource):
    def get(self):
        resultado = CanchitaModel.query.all()
        if resultado:            
            arregloResultado = []
            for item in resultado:
                arregloResultado.append(item.retornar_json())
            print(arregloResultado) 
            return arregloResultado
        print(resultado)
        return {'message':'No se pudo conseguir'}