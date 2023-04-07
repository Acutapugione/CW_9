import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') \
        or '123456512' 
    SQLALCHEMY_DATABASE_URI = 'sqlite:///my_database.db'
    #mysql://username:password@server/db

# print(Config.SECRET_KEY)