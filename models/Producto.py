from db import db

class Producto(db.Model):
    __tablename__ = 'productos'
    id_producto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    precio = db.Column(db.Numeric)
    descripcion = db.Column(db.String)
    imagen = db.Column(db.String)

    def __init__(self, nombre, precio, descripcion, imagen):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.imagen = imagen