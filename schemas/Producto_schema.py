from ma import ma
from models.Producto import Producto

class ProductoSchema(ma.Schema):
    class Meta:
        model = Producto
        fields = ('id_producto',
                  'nombre',
                  'precio',
                  'descripcion',
                  'imagen')

Producto_Schema = ProductoSchema()
Productos_Schema = ProductoSchema(many=True)