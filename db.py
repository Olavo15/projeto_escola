from pony.orm import Database

db = Database()
db.bind(provider='sqlite', filename='escola.db', create_db=True)
