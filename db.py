from codecs import ignore_errors
import sqlite3
from conf import DB

c = sqlite3.connect(DB)
ex = c.cursor()

try:
    ex.execute("CREATE TABLE users (id, last_user, session_key, scrobbling)")
except Exception as error:
    if str(error) != "table user already exists":
        print("Erro ao criar banco de dados: "+str(error))
    
c.commit()
c.close()