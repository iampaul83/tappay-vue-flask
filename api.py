from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import requests

import os
PARTNER_KEY = os.environ['PARTNER_KEY']

app = Flask(__name__)
api = Api(app)

ITEMS = {
    '1': {'name': 'TapPay T-shirt', 'amount': 999},
    '2': {'name': 'TapPay X-shirt', 'amount': 9999},
    '3': {'name': 'Tappay Z-shirt', 'amount': 99999},
}

def pay_by_prime(prime, item):
    url = 'https://sandbox.tappayapis.com/tpc/partner/directpay/paybyprime'
    headers = {'x-api-key': PARTNER_KEY}
    data = {
        'prime': prime,
        'partnerkey': PARTNER_KEY,
        'merchantid': '24951774_CTBC',
        'amount': item['amount'],
        'currency': 'TWD',
        'details': item['name'],
        'cardholder': {
            'phonenumber': '+886923456789',
            'name': '王小明',
            'email': 'LittleMing@Wang.com',
            'zip': '100',
            'addr': '台北市天龍區芝麻街1號1樓',
            'nationalid': 'A123456789'
        },
        'instalment': 0,
        'remember': False
    }
    r = requests.post(url, json=data, headers=headers)
    return r.json()

def abort_if_todo_doesnt_exist(item_id):
    if item_id not in ITEMS:
        abort(404)

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('amount')


# Todo
# shows a single todo item and lets you delete a todo item
class Item(Resource):
    def get(self, item_id):
        abort_if_todo_doesnt_exist(item_id)
        return ITEMS[item_id]

    def delete(self, item_id):
        abort_if_todo_doesnt_exist(item_id)
        del ITEMS[item_id]
        return '', 204

    def put(self, item_id):
        args = parser.parse_args()
        item = {'name': args['name'], 'amount': args['amount']}
        ITEMS[item_id] = item
        return item, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class ItemList(Resource):
    def get(self):
        return ITEMS

    # def post(self):
    #     args = parser.parse_args()
    #     item_id = int(max(ITEMS.keys()).lstrip('todo')) + 1
    #     item_id = 'todo%i' % item_id
    #     ITEMS[item_id] = {'task': args['task']}
    #     return ITEMS[item_id], 201

parser2 = reqparse.RequestParser()
parser2.add_argument('prime')
class PayByPrime(Resource):
    def post(self, item_id):
        abort_if_todo_doesnt_exist(item_id)
        args = parser2.parse_args()
        item = ITEMS[item_id]
        prime = args['prime']
        result = pay_by_prime(prime, item)
        return result

##
## Actually setup the Api resource routing here
##
api.add_resource(ItemList, '/items')
api.add_resource(Item, '/items/<item_id>')
api.add_resource(PayByPrime, '/pay/<item_id>')


if __name__ == '__main__':
    app.run(debug=True)