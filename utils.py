from models import Pessoas, Atividades


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


if __name__ == '__main__':
    # insert_person()
    # update_person()
    # delete_person()
    search_person()