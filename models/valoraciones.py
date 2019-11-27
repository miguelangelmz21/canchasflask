from base_de_Datos import bd

class ValoracionesModel(bd.Model):
    __tablename__="t_valoraciones"
    val_id = bd.Column(bd.Integer,primary_key=True)
    val_comentario = bd.Column(bd.Text)
    val_estrellas = bd.Column(bd.Integer)
    res_id = bd.Column(bd.Integer,bd.ForeignKey('t_reserva.res_id'),nullable=False)
   

    def __init__(self,comentario,estrellas,id_res):
        self.comentario=comentario
        self.estrellas = estrellas
        self.res_id = id_res

    def retornar_json(self):
        return {
            'id':self.tipo_id,
            'descripcion':self.tipo_desc
        }
        
    def guardar_en_la_bd(self):
        bd.session.add(self)        
        bd.session.commit()