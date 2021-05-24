from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# db_string = "postgres://admin:donotusethispassword@aws-us-east-1-portal.19.dblayer.com:15813/compose"
db_string = 'sqlite:///atividades.db'
engine = create_engine(db_string)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))


base = declarative_base()
base.query = db_session.query_property()

class Pessoas(base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), index=True)
    age = Column(Integer)
    
    def __repr__(self):
        return f'<Pessoas {self.name}>'
    
    def save(self):
        db_session.add(self)
        db_session.commit()
    
    def delete(self):
        db_session.delete(self)
        db_session.commit()
    

class Atividades(base):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pssoa = relationship('Pessoas')
    

def init_db():
    base.metadata.create_all(bind=engine)
    

if __name__ == '__main__':
    init_db()