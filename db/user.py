from .database import engine
from .schema import User
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
import uuid, bcrypt

class USER:
    def __init__(self):
        pass

    def createRootUser(self):
        my_uuid = uuid.uuid4()
        my_password = "Tin2025"
        password_bytes = my_password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        my_password = hashed_password.decode('utf-8')
        new_user = User(
            id=my_uuid.hex, 
            name='Sokhavuth',
            email='sokhavuth@khmerweb.app',
            password=my_password,
            role='Admin',
            thumb='',
            content='',
            date=''
        )
        session.add(new_user)

user = USER()