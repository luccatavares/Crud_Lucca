from database import db

class Viagem(db.Model):
    _tablename_= "viagem"
    id_pacote = db.Column(db.Integer, primary_key = True)
    destino = db.Column(db.String(100))
    data_saida = db.Column(db.Date)
    preco = db.Column(db.Float(10,2))

    def __init__(self, destino, data_saida, preco):
        self.destino = destino
        self.data_saida = data_saida
        self.preco = preco

    def _repr_(self):
        return "<Destino: {}>".format(self.destino)