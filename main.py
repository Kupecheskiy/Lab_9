from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask('Jobs list')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(300))
    term = db.Column(db.Integer)


    def __repr__(self):
        return f'Company{self.id}. {self.company_name} - {self.term} months.'


# products = [
#     {'prod_name': 'Диван',
#      'price': 12000,
#      'in_stock': False,
#      'id': 0},
#     {'prod_name': 'Стол',
#      'price': 7000,
#      'in_stock': True,
#      'id': 1},
#     {'prod_name': 'Стул',
#      'price': 3000,
#      'in_stock': False,
#      'id': 2},
# ]


@app.route('/')
def main():
    companies = Company.query.all()
    return render_template('index.html', companies_list=companies)


# @app.route('/in_stock/<int:product_id>', methods=['PATCH'])
# def modify_product(product_id):
#     product = Product.query.get(product_id)
#     product.in_stock = request.json['in_stock']
#     db.session.commit()
#     # global products
#     # in_stock = request.json['in_stock']
#     # for product in products:
#     #     if product['id'] == product_id:
#     #         product.update({'in_stock': in_stock})
#     return "Ok"


@app.route('/add', methods=['POST'])
def add_company():
    data = request.json
    company = Company(**data)
    db.session.add(company)
    db.session.commit()
    # print(data)
    # id_last = products[-1]['id']
    # id_new = id_last + 1
    # data['id'] = id_new
    # products.append(data)
    return 'Ok'


@app.route('/clear', methods=['DELETE'])
def clear_companies():
    db.session.query(Company).delete()
    db.session.commit()
    return 'Ok'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)