from flask import Flask, request, jsonify
from models import db, Product
from schemas import product_schema, products_schema
from database import init_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db.init_app(app)
init_db(app)

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    product = Product(**data)
    db.session.add(product)
    db.session.commit()
    return product_schema.jsonify(product), 201

@app.route('/products', methods=['GET'])
def get_products():
    page = request.args.get('page', 1, type=int)
    size = request.args.get('size', 10, type=int)
    products = Product.query.paginate(page, size, False).items
    return products_schema.jsonify(products), 200

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return product_schema.jsonify(product), 200

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    product = Product.query.get_or_404(product_id)
    for key, value in data.items():
        setattr(product, key, value)
    db.session.commit()
    return product_schema.jsonify(product), 200

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
