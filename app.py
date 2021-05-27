from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades, Users
from flask_httpauth import HTTPBasicAuth


auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

# users = {
#     'fulano': 'senha',
#     'juao': 'senha',
# }

# @auth.verify_password
# def verify_auth(username, passwd):
#     if not (username, passwd):
#         return False
#     return users.get(username) == passwd

@auth.verify_password
def verify_auth(username, password):
    if not (username, password):
        return False
    return Users.query.filter_by(username=username, password=password).first()
class Person(Resource):
    
    @auth.login_required
    def get(self, name):
        person = Pessoas.query.filter_by(name=name).first()
        try:
            response = {
                'name': person.name,
                'age': person.age,
                'id': person.id
            }
        except AttributeError:
            response = {
                'Status': 'error',
                'Message': 'person not fould'
            }
        return response
    
    @auth.login_required
    def put(self, name):
        person = Pessoas.query.filter_by(name=name).first()
        data = request.json
        if 'name' in data:
            person.name = data['name']
        if 'age' in data:
            person.age = data['age']
        
        person.save()
        response = {
            'id': person.id,
            'name': person.name,
            'age': person.age
        }  
        return response
    
    @auth.login_required
    def delete(self, name):
        person = Pessoas.query.filter_by(name=name).first()
        person.delete()
        msg = f'Person {person.name} deleted with sucess.'
        return {'status': 'sucess', 'message': msg}


class Persons(Resource):
    
    @auth.login_required
    def get(self):
        persons = Pessoas.query.all()
        response = [{'id': i.id, 'name': i.name, 'age': i.age} for i in persons]
        return response
    
    @auth.login_required
    def post(self):
        data = request.json
        person = Pessoas(name=data['name'], age=data['age'])
        person.save()
        response = {
            'id': person.id,
            'name': person.name,
            'age': person.age
        }
        
        return response


class Activities(Resource):
    def get(self):
        activities = Atividades.query.all()
        response = [{'id': i.id, 'person': i.pessoa.name, 'atividade': i.name }for i in activities]
        return response
    
    def post(self):
        data = request.json
        person = Pessoas.query.filter_by(name=data['person']).first()
        activities = Atividades(name=data['name'], pessoa=person)
        activities.save()
        response = {
            'id': activities.id,
            'person': activities.pessoa.name,
            'name': activities.name
        }
        return response


api.add_resource(Person, '/person/<string:name>/')
api.add_resource(Persons, '/persons/')
api.add_resource(Activities, '/activities/')

if __name__ == '__main__':
    app.run(debug=True)
