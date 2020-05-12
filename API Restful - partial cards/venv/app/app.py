from flask import Flask, jsonify, make_response, render_template
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

customers = [
    {
        "First name": "George",
        "E-mail": "kar.giorgos7@hotmail.com",
        "Trailing card digits": "3456",
        "Leading card digits": "4536",
        "Card type": "Mastercard",
        "Start card date": "08.2017",
        "Expiry card date": "08.2020"
    },
    {
        "First name": "Nick",
        "E-mail": "nick888@hotmail.com",
        "Trailing card digits": "1336",
        "Leading card digits": "0446",
        "Card type": "Mastercard",
        "Start card date": "08.2017",
        "Expiry card date": "08.2020"
    },
    {
        "First name": "Max",
        "E-mail": "max887@hotmail.com",
        "Trailing card digits": "2416",
        "Leading card digits": "5536",
        "Card type": "Mastercard",
        "Start card date": "08.2018",
        "Expiry card date": "08.2021"
    },
    {
        "First name": "Alex",
        "E-mail": "alexxx98@outlook.com",
        "Trailing card digits": "3456",
        "Leading card digits": "1819",
        "Card type": "Visa",
        "Start card date": "02.2018",
        "Expiry card date": "02.2021"
    },
    {
        "First name": "Maria",
        "E-mail": "mariak1998@gmail.com",
        "Trailing card digits": "1336",
        "Leading card digits": "2719",
        "Card type": "Visa",
        "Start card date": "01.2019",
        "Expiry card date": "01.2022"
    },
    {
        "First name": "Olga",
        "E-mail": "olga2000@outlook.com",
        "Trailing card digits": "2416",
        "Leading card digits": "5029",
        "Card type": "Visa",
        "Start card date": "03.2019",
        "Expiry card date": "03.2022"
    }
]

@app.route('/')
def index():
    return render_template('home.html')

class Customer(Resource):
    def get(self, trailingCardDigits):
        cust = [customer for customer in customers if customer['Trailing card digits'] == trailingCardDigits]
        for customer in cust:
            if (customer['Trailing card digits'] == trailingCardDigits):
                return make_response(jsonify(cust), 200)
        return "Customer not found", 404

    def put(self,trailingCardDigits,email):
        parser = reqparse.RequestParser()
        parser.add_argument("firstName")
        parser.add_argument("trailingCardDigits")
        parser.add_argument("leadingCardDigits")
        parser.add_argument("cardType")
        parser.add_argument("startCardDate")
        parser.add_argument("expiryCardDate")
        args = parser.parse_args()

        for customer in customers:
            if(trailingCardDigits == customer["Trailing card digits"] and email == customer["E-mail"]):
                customer["First name"] = args["firstName"]
                customer["Trailing card digits"] = args["trailingCardDigits"]
                customer["Leading card digits"] = args["leadingCardDigits"]
                customer["Card type"] = args["cardType"]
                customer["Start card date"] = args["startCardDate"]
                customer["Expiry card date"] = args["expiryCardDate"]
                return make_response(jsonify(customer), 200)
        
        customer = {
            "E-mail": email,
            "First name": args["firstName"],
            "Trailing card digits": args["trailingCardDigits"],
            "Leading card digits": args["leadingCardDigits"],
            "Card type": args["cardType"],
            "Start card date": args["startCardDate"],
            "Expiry card date": args["expiryCardDate"]
        }
        
        customers.append(customer)
        return make_response(jsonify(customer), 201)
    
api.add_resource(Customer, "/customer/<string:trailingCardDigits>", endpoint="/customer/<string:trailingCardDigits>", methods=['GET'])
api.add_resource(Customer, "/customer/<string:trailingCardDigits>/<string:email>", endpoint="/customer/<string:trailingCardDigits>/<string:email>", methods=['PUT'])
if __name__ == '__main__':
    app.debug = True
    app.run()
