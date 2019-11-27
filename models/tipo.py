from base_de_Datos import bd

class TipoModel(bd.Model):
    __tablename__="t_tipo"
    tipo_id = bd.Column(bd.Integer,primary_key=True)
    tipo_desc = bd.Column(bd.String(45),nullable=True)
    canchitas = bd.relationship('CanchitaModel',lazy=True, backref='tipos')
    #es una manera simple de declarar una nueva propiedad en la clase canchitasModel para poder ingresar a sus valores solamente necesitaria canchita.tipo

    def __init__(self,descripcion):
        self.tipo_desc=descripcion

    def retornar_json(self):
        return {
            'id':self.tipo_id,
            'descripcion':self.tipo_desc
        }
    def retornar_json_con_nombre_local(self):
        nombres = []
        for canchita in self.canchitas:
            nombres.append(canchita.local.loc_nombre)
        return {
            'descripcion':self.tipo_desc,
            'nombres':nombres
        }

    def retornar_json_con_nombre__lat_lng_local(self):
        lugares = []
        for canchita in self.canchitas:
            lugares.append( {
                'nombre':canchita.local.loc_nombre,
                'lat':str(canchita.local.loc_lat),
                'lng':str(canchita.local.loc_lng)
            })
        listaNuevaLocales = []
        for lugar in lugares:
            if lugar not in listaNuevaLocales:
                listaNuevaLocales.append(lugar)            
        return {
            'descripcion':self.tipo_desc,
            'lugares':listaNuevaLocales
        }

    def guardar_en_la_bd(self):
        bd.session.add(self)
        bd.session.commit()