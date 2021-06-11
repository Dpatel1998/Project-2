from application import db
from application.models import Soldier

db.drop_all()
db.create_all()