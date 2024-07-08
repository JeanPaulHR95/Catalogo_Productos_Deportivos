from flask import Blueprint
from flask import request, make_response
from flask import jsonify
from flask import jsonify
from models.Producto import Producto
from schemas.Producto_schema import Productos_Schema

producto = Blueprint('Productos', __name__)

@producto.route('/Obtenerproductos', methods = ['GET'])
def GetProductos():
    productos = Producto.query.all()
    resultado = Productos_Schema.dump(productos)
    response ={
       'success': True,
        'data': resultado   
    }    
    return make_response(jsonify(response),201)
