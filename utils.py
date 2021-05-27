from models import Pessoas, Atividades, Users


def insert_person():
    pessoa = Pessoas(name='Erica', age=27)
    pessoa.save()
    print(pessoa)


def search_person():
    pessoa = Pessoas.query.all()
    print(pessoa)
    # pessoa = Pessoas.query.filter_by(name='Erica').first()
    # print(f'name: {pessoa.name} - Age: {pessoa.age}')


def update_person():
    pessoa = Pessoas.query.filter_by(name='Erica').first()
    print(pessoa)
    pessoa.age = 25
    pessoa.save()
    
def delete_person():
    person = Pessoas.query.filter_by(name='Erica').first()
    person.delete()


def insert_user(username, password):
    user = Users(username=username, password=password)
    user.save()
    
def select_users():
    users = Users.query.all()
    print(users)

if __name__ == '__main__':
    # insert_person()
    # update_person()
    # delete_person()
    # search_person()
    insert_user('fulano', 'senha')
    insert_user('juao', 'senha')
    select_users()