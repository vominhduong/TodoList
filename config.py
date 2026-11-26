import os
DirPath=os.path.dirname(os.path.abspath(__file__))
class Config:
    #db config
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(DirPath, 'todo.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False